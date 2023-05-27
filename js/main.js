console.log("Hello World")

// Parse the XML file
var parser = new DOMParser();

// Getting the users current date and time
var userDate = new Date();
var file;

function present(){
    console.log("Hello")
}

function formattedDate(d = new Date) {
    let month = String(d.getMonth() + 1);
    let day = String(d.getDate());
    const year = String(d.getFullYear());
  
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
  
    return `${year}-${month}-${day}`;
  }

// Stores the info
function processData(data){
    file = data;

    //Converting the string to XML below
    var doc = parser.parseFromString(file, "application/xml")
    var dates = doc.getElementsByTagName("Date")
    console.log(dates)
    var newDates = [];
    console.log(dates)
    for(var x = 0; x < dates.length; x++){
        let allDates = new Date(dates[x].textContent)

        // Filters dates by Sunday 
        if(allDates.getDay() == 0){
            newDates.push(new Date(dates[x].textContent))
        } 
    }
    
    console.log(newDates);
    // console.log(dates);
    // Find nearest date
    var temp = newDates.map(d => Math.abs(new Date() - new Date(d).getTime()));
    var idx = temp.indexOf(Math.min(...temp));
    var nextRaceDate = formattedDate(newDates[idx])
    console.log(nextRaceDate)

    var gps = doc.getElementsByTagName("Race")
    console.log(gps)

    for(var i = 0; i < gps.length; i++){
        var gp = gps[i];
        var date = gp.getElementsByTagName("Date")[0].textContent

        if(date == nextRaceDate){
            console.log(date)
        }
    }

    // var raceweekend = doc.getElementsByText("Date")
    // console.log(raceweekend)
}

function getResults(){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
    var result = fetch("http://ergast.com/api/f1/current", requestOptions)
        .then(response => response.text())
        .then(result => processData(result))
        .catch(error => console.log('error', error));

    xml = parser.parseFromString(result, "text/xml");
    var tags = xml.querySelectorAll("date")
    // console.log(tags)
}

getResults()

