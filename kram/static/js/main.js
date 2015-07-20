// Main script

var kram = kram || {};

// Using only single function right now

kram.xVal = 0;
kram.yVal = 0;

// Setup graph
kram.chart = new CanvasJS.Chart("func-plot", {
		backgroundColor: "#191919",	
		data: [{
				type: "line",
				dataPoints: kram.data.series
		}]
});

$(document).ready(function() {

    // Fill stats
    kram.updateStat();
    kram.setFunction("-");
    kram.setTitle("-");
    
    // Vertical tab grouping
    $(".nav-stacked a").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });

    // Bind SSE event
    var evtSrc = new EventSource("/subscribe");
    evtSrc.onmessage = function(e) {

        // Set starting time
        if (kram.data.beginTime == "NA") {        
            kram.data.beginTime = new Date();
        }
        
        data = JSON.parse(e.data);
        kram.xVal = data.x;
        kram.yVal = data.y;
        kram.updateChart();
        kram.setFunction(data.func);
        kram.setTitle(data.title);
    };

    // Shutdown the server
    $("#shutdown-btn").click(function() {
        $.get("/stop", function(data){
            if (data == "ok") {
                alert("Server successfully stopped");
            }
            else {
                alert("Error : " + data);
            }
        });
    });

    // Update stats
    $("#stats-btn").click(function() {
        kram.calculateStats();
        kram.updateStat();
    });
    
    $(".refresh-btn").click(function() {
        kram.calculateStats();
        kram.updateStat();
    })
});

