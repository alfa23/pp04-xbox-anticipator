// roundSlider script: http://roundsliderui.com

$("#handle1").roundSlider({
    sliderType: "min-range",
    editableTooltip: false,
    radius: 100,
    width: 23,
    min: 0,
    max: 5,
    step: 0.1,
    value: 0,
    handleSize: 0,
    handleShape: "square",
    circleShape: "pie",
    startAngle: 315,
    beforeCreate: "traceEvent",
    create: "traceEvent",
    start: "traceEvent",
    stop: "traceEvent",
    change: "traceEvent",
    drag: "traceEvent",
    valueChange: "traceEvent",
    tooltipFormat: "changeTooltip",
    
    svgMode: true,
	  borderWidth: 0,
	  pathColor: "#d9f9fa",
	  // rangeColor: "#A6CF93",
	  rangeColor: "url(#slider1_range_grad)",
});

function changeTooltip(e) {
    var val = e.value, speed;
    if (val < 1) speed = "COLD";
    else if (val < 2) speed = "TEPID";
    else if (val < 3) speed = "WARM";
    else if (val < 4) speed = "HOT";
    else speed = "SCORCHING!";

    return val + "<div>" + speed + "<div>";
}

function traceEvent(e) {
		var val = e.value
    console.log(e.type);
    console.log(val);
}
