var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});


L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
}).addTo(myMap);

function markerSize(price) {
    return price/2;
}

d3.csv("Resources/new-york-city-airbnb-open-data/AB_NYC_2019.csv", function(error, data) {
    if(error) throw error;
    for (var i=0; i<data.price.length; i++) {
        L.circle(data[i].location, {
            fillOpacity: .75,
            color: "white",
            fillColor: "purple",
            radius: markerSize(data[i].price)
        }).bindPopup("<h1>" + data[i].name + "</h1> <hr> <h3>Population: " + data[i].price+ "</h3>").addTo(myMap);
    }
});

