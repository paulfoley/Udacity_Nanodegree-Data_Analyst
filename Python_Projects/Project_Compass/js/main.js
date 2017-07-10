// Google Maps Script
google.maps.event.addDomListener(window, 'load', initMap);


function initMap() {
  var goldengate = {lat: 37.8197, lng:  -122.4786};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    scrollwheel: false,
    center: goldengate,
// Style taken from Snazzy Maps 
    styles: [
{
    "featureType": "administrative",
    "elementType": "all",
    "stylers": [
        {
            "visibility": "on"
        },
        {
            "lightness": 33
        }
    ]
},
{
    "featureType": "landscape",
    "elementType": "all",
    "stylers": [
        {
            "color": "#f2e5d4"
        }
    ]
},
{
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#c5dac6"
        }
    ]
},
{
    "featureType": "poi.park",
    "elementType": "labels",
    "stylers": [
        {
            "visibility": "on"
        },
        {
            "lightness": 20
        }
    ]
},
{
    "featureType": "road",
    "elementType": "all",
    "stylers": [
        {
            "lightness": 20
        }
    ]
},
{
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#c5c6c6"
        }
    ]
},
{
    "featureType": "road.arterial",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#e4d7c6"
        }
    ]
},
{
    "featureType": "road.local",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#fbfaf7"
        }
    ]
},
{
    "featureType": "water",
    "elementType": "all",
    "stylers": [
        {
            "visibility": "on"
        },
        {
            "color": "#acbcc9"
        }
    ]
}
]
  });
// Map Pins Locations, Images, and Descriptions
  var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h2 id="firstHeading" class="firstHeading">Golden Gate Bridge</h2>'+
      '<div id="bodyContent">'+
      '<p>The Golden Gate Bridge was one of my favorite sites in San Franscisco</p>'+
      '<img height="150px" width="200px" src="img/Golden-Gate-Bridge.jpg">'
      '</div>'+
      '</div>';

  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  var marker = new google.maps.Marker({
    position: goldengate,
    map: map,
    title: 'Golden Gate Bridge'
  });
  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
}
