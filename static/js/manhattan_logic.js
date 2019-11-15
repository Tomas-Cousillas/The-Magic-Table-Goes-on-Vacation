console.log("manhattan js")

// Initialize an array to hold airbnb markers and entire house markers
var airbnbMarkers = [];
var entireHouseMarkers = [];
var heatArray = [];

// An array of cities and their locations
function createMarkers(response) {

  // Filter by "Entire home/apt"
  var filteredEntireHouseResponse = response.filter((entry => entry.room_type === "Entire home/apt"))
  console.log(filteredEntireHouseResponse.length)
  // Loop through the airbnb array
  for (var i = 0; i < filteredEntireHouseResponse.length; i++) {
    if (i < 50) {
      var airbnb = filteredEntireHouseResponse[i];
      //For each airbnb, create a marker and bind a popup with the airbnbs name and price
      var airbnbMarker = L.marker([airbnb.latitude, airbnb.longitude]).bindPopup("<h3> <font color= black>" + airbnb.name + "</font> <h3>" + "<h3> <font color= black> Price: $" + airbnb.price + " per night" + "</font><h3>");
      //Add the marker to the airbnbMarkers array
      entireHouseMarkers.push(airbnbMarker);
    }
  }
  // Loop through the airbnb array
  for (var i = 0; i < response.length; i++) {
    if (i < 200) {
      var airbnb = response[i];
      //For each airbnb, create a marker and bind a popup with the airbnbs name and price
      var airbnbMarker = L.marker([airbnb.latitude, airbnb.longitude]).bindPopup("<h3> <font color= black>" + airbnb.name + "</font> <h3>" + "<h3> <font color= black> Price: $" + airbnb.price + " per night" + "</font><h3>");
      //Add the marker to the airbnbMarkers array
      airbnbMarkers.push(airbnbMarker);
    }
  }
// Create heat map
    for (var i = 0; i < response.length; i++) {
      var airbnb = response[i];
      heatArray.push([airbnb.latitude, airbnb.longitude]);
    }
};
  
fetch("http://127.0.0.1:5000/Manhattan", {
  "Access-Control-Allow-Origin": "*"
})
  .then(data => {
    return data.json()
  })
  .then(function (data) {
    // console.log(data);
    createMarkers(data)

    // Define variables for our tile layers
    var emptyGroup = L.layerGroup([])
    var allListingGroup = L.layerGroup(airbnbMarkers)
    var entireHouseGroup = L.layerGroup(entireHouseMarkers)
    var heatGroup = L.layerGroup(heat)

    var allListingsLayer = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.dark",
      accessToken: API_KEY
    });

    var entireHouseLayer = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.dark",
      accessToken: API_KEY
    });

    var heat_Layer = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.streets",
      accessToken: API_KEY
    });

    var heat = L.heatLayer(heatArray, {
      radius: 20,
      blur: 35
    }).addTo(heatGroup);

    // Only one base layer can be shown at a time
    var baseMaps = {
      none: emptyGroup
    };

    // Overlays that may be toggled on or off
    var overlayMaps = {
      All: allListingGroup,
      EntireHouse: entireHouseGroup,
      Heat: heatGroup
    };

    // Create map object and set default layers
    var myMap = L.map("map", {
      center: [40.6782, -73.9442],
      zoom: 12,
      layers: [allListingsLayer, entireHouseLayer, heat_Layer]
    });

    // Pass our map layers into our layer control
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
    

//   .catch (function (error) {
//   console.log(error);
});