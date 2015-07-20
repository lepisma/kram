// Calculations and stuff

var kram = kram || {};

kram.calculateStats = function() {
    // Modify only if enough data are available
    // Doesn't consider the data update between calculation
    if (kram.data.series.length > 1) {
        var minidx = 0;
        var min = kram.data.series[minidx].y;
        var maxidx = 0;
        var max = kram.data.series[maxidx].y;
        var mean = 0;

        for (var i = 0; i < kram.data.series.length; i++) {
            mean += kram.data.series[i].y;
            if (kram.data.series[i].y < min) {
                min = kram.data.series[i].y;
                minidx = i;
            }

            if (kram.data.series[i].y > max) {
                max = kram.data.series[i].y;
                maxidx = i;
            }
        }
        
        mean /= kram.data.series.length;

        // Update data
        if (kram.data.max.value != "NA") {
            if (kram.data.max.value < max) {
                kram.data.max.style = 0;
            }
            else {
                kram.data.max.style = 1;
            }
        }
        kram.data.max.value = max;
        kram.data.max.run = maxidx;

        if (kram.data.min.value != "NA") {
            if (kram.data.min.value > min) {
                kram.data.min.style = 2;
            }
            else {
                kram.data.min.style = 1;
            }
        }
        kram.data.min.value = min;
        kram.data.min.run = minidx;
        
        if (kram.data.mean.value != "NA") {
            if (kram.data.mean.value < mean) {
                kram.data.mean.style = 0;
            }
            else if (kram.data.mean.value > mean) {
                kram.data.mean.style = 2;
            }
            else {
                kram.data.mean.style = 1;
            }
        }
        kram.data.mean.value = mean;
    }
}
