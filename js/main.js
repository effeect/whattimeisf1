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
    console.log(gp_date)
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

    field_names = [ ["raceName", gp_object.race_name],
                    ["Date",gp_object.date],
                    ["raceTime",gp_object.time_of_race],
                    ["qualiTime",gp_object.quali.qual_time],
                    ["fp1Time",gp_object.fp1.fp1_time],
                    ["fp2Time",gp_object.fp2.fp2_time],
                    ["fp3Time",gp_object.fp3.fp3_time]
                ]

    for(var i = 0; i < field_names.length; i++){
        field_name = field_names[i]
        console.log(field_name[0])
        replaceText(field_name[0],field_name[1])
    }            
    

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
      
    var result = fetch("http://ergast.com/api/f1/current", requestOptions)
        .then(response => response.text())
        .then(result => processData(result))
        .catch(error => console.log('error', error));

    xml = parser.parseFromString(result, "text/xml");
    var tags = xml.querySelectorAll("date")
    // console.log(tags)
}

getResults()

