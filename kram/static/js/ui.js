// UI updation functions

var kram = kram || {};

// Styles for stats
kram.statStyle = [
    {
        color: "text-success",
        icon: "glyphicon-chevron-up"
    },
    {
        color: "text-info",
        icon: "glyphicon-minus"
    },
    {
        color: "text-warning",
        icon: "glyphicon-chevron-down"
    }
];

// Set the experiment title
kram.setTitle = function(title) {
    $("#experiment-name").text(title);
}

// Set the function name
kram.setFunction = function(name) {
    $("#plots .plot .plot-title > h4").text(name);
    $("#details .panel-title").text(name);
}

// Update the stat pane
kram.updateStat = function() {
    // Update max, min and mean

    var maxDiv = $("#details .stat-row:eq(0) h1");
    var minDiv = $("#details .stat-row:eq(1) h1");
    var meanDiv = $("#details .stat-row:eq(2) h1");
    
    maxDiv.removeClass();
    maxDiv.addClass(kram.statStyle[kram.data.max.style].color);
    maxDiv.html("<span class='glyphicon " + kram.statStyle[kram.data.max.style].icon + "'></span> " + (Math.floor(kram.data.max.value * 100) / 100));

    minDiv.removeClass();
    minDiv.addClass(kram.statStyle[kram.data.min.style].color);
    minDiv.html("<span class='glyphicon " + kram.statStyle[kram.data.min.style].icon + "'></span> " + (Math.floor(kram.data.min.value * 100) / 100));

    meanDiv.removeClass();
    meanDiv.addClass(kram.statStyle[kram.data.mean.style].color);
meanDiv.html("<span class='glyphicon " + kram.statStyle[kram.data.mean.style].icon + "'></span> " + (Math.floor(kram.data.mean.value * 100) / 100));
    
    $("#details .run-max").text(kram.data.max.run);
    $("#details .run-min").text(kram.data.min.run);
    
    // Update runtime
    $(".runtime").text(kram.data.runtime);
    $(".beginTime").text(kram.data.beginTime);
    $(".perRunTime").text(kram.data.perRunTime);
    $(".runs").text(kram.data.runs);
}

// Update the live chart
kram.updateChart = function() {
    kram.data.series.push({
        x: kram.xVal,
        y: kram.yVal
    });
    
		kram.chart.render();
};
