
var event_date = new Date(2016, 07, 22, 18, 30);
 
db.events.insert(
{'date': event_date.toISOString(),'name': "PhillyMUG: June",
"loc" : {
       "type" : "Point",
       "coordinates" : [ -73.778889, 40.639722 ]
},
"messages": [
{
  "daysleft": 1,
  "message": "Only 1 more day until PhillyMUG June!",
  "image": "http://localhost:5001/mug/static/images/1.png"
},
{
  "daysleft": 5,
  "message": "5 more days until PhillyMUG June! Signup Today.",
  "image": "http://localhost:5001/mug/static/images/5.png"
},
{
  "daysleft": 10,
  "message": "10 more days until PhillyMUG June! Signup Today.",
  "image": "http://localhost:5001/mug/static/images/10.png"
},
{
  "daysleft": 15,
  "message": "15 more days until PhillyMUG June! Signup Today.",
  "image": "http://localhost:5001/mug/static/images/15.png"
},
{
  "daysleft": 20,
  "message": "20 more days until PhillyMUG June! Signup Today.",
  "image": "http://localhost:5001/mug/static/images/20.png"
},
{
  "daysleft": 22,
  "message": "22 more days until PhillyMUG June! Signup Today.",
  "image": "http://localhost:5001/mug/static/images/22.png"
}
],
})
