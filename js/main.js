// To Parse the XML file
var parser = new DOMParser();

// Getting the users current date and time
var userDate = new Date();
var file;


function formattedDate(d = new Date) {
    let month = String(d.getMonth() + 1);
    let day = String(d.getDate());
    const year = String(d.getFullYear());
  
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
  
    return `${year}-${month}-${day}`;
  }

function removeLastCharacter(string){
    let result = string.slice(0,-1);
    return result
}
// Stores the info
function processData(data){
    file = data;

    //Converting the string to XML below
    var doc = parser.parseFromString(file, "application/xml")
    var dates = doc.getElementsByTagName("Date")
    var newDates = [];
    for(var x = 0; x < dates.length; x++){
        let allDates = new Date(dates[x].textContent)

        // Filters dates by Sunday 
        if(allDates.getDay() == 0){
            newDates.push(new Date(dates[x].textContent))
        } 
    }
    
    var closest = Infinity;
    newDates.forEach(date => {
        if(date >= userDate.setHours(userDate.getHours() - 3) && date < closest) {
            closest = date
            console.log(closest)
            console.log(userDate.setHours(userDate.getHours() - 3))
        }
    })

    var nextRaceDate = formattedDate(closest)
    // Uncoment for Debugging 
    //console.log(`The next race is now : ${nextRaceDate}`)

    var gps = doc.getElementsByTagName("Race")
    var gp_date;

    for(var i = 0; i < gps.length; i++){
        var gp = gps[i];
        var date = gp.getElementsByTagName("Date")[0].textContent

        if(date == nextRaceDate){
            console.log(`Next race is ${date}`)
            gp_date = gp
        }
    }

    // Below we create the GP object
    let gp_object ={
        race_name : gp_date.getElementsByTagName("RaceName")[0].textContent,
        date : gp_date.getElementsByTagName("Date")[0].textContent,
        time_of_race : gp_date.getElementsByTagName("Time")[0].textContent,
        fp1 : {
            fp1_time : gp_date.getElementsByTagName("Time")[1].textContent
        },
        fp2 : {
            fp2_time : gp_date.getElementsByTagName("Time")[2].textContent
        },
        fp3 : {
            fp3_time : gp_date.getElementsByTagName("Time")[3].textContent
        },
        quali : {
            qual_time : gp_date.getElementsByTagName("Time")[4].textContent
        }
    } 

    dateObjectRepresent(closest,gp_object.time_of_race)

    field_names = [ ["raceName", gp_object.race_name],
                    ["Date",gp_object.date],
                    ["raceTime",dateObjectRepresent(closest,gp_object.time_of_race)],
                    ["qualiTime",dateObjectRepresent(closest,gp_object.quali.qual_time)],
                    ["fp1Time",dateObjectRepresent(closest,gp_object.fp1.fp1_time)],
                    ["fp2Time",dateObjectRepresent(closest,gp_object.fp2.fp2_time)],
                    ["fp3Time",dateObjectRepresent(closest,gp_object.fp3.fp3_time)]
                ]

    for(var i = 0; i < field_names.length; i++){
        field_name = field_names[i]
        replaceText(field_name[0],field_name[1])
    }            
    

}

// Function to create a Date Format session
function dateObjectRepresent(date,time){
    let dateTrim = date.toLocaleString().split(',')[0].trim().split(/[\/ ]/)
    let timeTrim = removeLastCharacter(time).split(":")
    
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date
    let dateObject = new Date(Date.UTC(dateTrim[2] , dateTrim[1] -1 , dateTrim[0] , timeTrim[0] , timeTrim[1] , timeTrim[2] ))
    let timeObject = dateObject.toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'});
    return timeObject;
}

function replaceText(fieldName, object_value){
    let fieldNameElement = document.getElementById(fieldName);
    fieldNameElement.innerHTML = object_value;
}

function getResults(){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
    var result = fetch("https://ergast.com/api/f1/current", requestOptions)
        .then(response => response.text())
        .then(result => processData(result))
        .catch(error => console.log('error', error));

    xml = parser.parseFromString(result, "text/xml");
    var tags = xml.querySelectorAll("date")
    // console.log(tags)
}

getResults()

