// // roundSlider script: http://roundsliderui.com
// $(document).ready(function() {

//     $("#handle1").roundSlider({
//         sliderType: "min-range",
//         editableTooltip: false,
//         radius: 100,
//         width: 23,
//         min: 0,
//         max: 5,
//         step: 0.1,
//         value: 0,
//         handleSize: 0,
//         handleShape: "square",
//         circleShape: "pie",
//         startAngle: 315,
//         beforeCreate: "traceEvent",
//         create: "traceEvent",
//         start: "traceEvent",
//         stop: "traceEvent",
//         change: "traceEvent",
//         drag: "traceEvent",
//         valueChange: "traceEvent",
//         tooltipFormat: "changeTooltip",
        
//         svgMode: true,
//         borderWidth: 0,
//         pathColor: "#d9f9fa",
//         // rangeColor: "#A6CF93",
//         rangeColor: "url(#slider1_range_grad)",
//     });

//     function changeTooltip(e) {
//         var val = e.value, temp;
//         if (val < 1) temp = "COLD";
//         else if (val < 2) temp = "TEPID";
//         else if (val < 3) temp = "WARM";
//         else if (val < 4) temp = "HOT";
//         else temp = "SCORCHING!";

//         return val + "<div>" + temp + "<div>";
//     }

//     function traceEvent(e) {
//             var val = e.value
//         console.log(e.type);
//         console.log(val);
//     }

//     // https://stackoverflow.com/questions/298772/django-template-variables-and-javascript
//     const initUserRate = '{{ current_user_rating }}';
//     console.log(initUserRate);
//     // console.log(myrate);

//     $("#handle1").roundSlider("option", "value", initUserRate);

//     // https://stackoverflow.com/questions/68063119/how-to-store-the-value-of-circular-slider-in-a-variable-and-display-it-in-consol
//     const getValue = (e) => {
//         let newUserRate = e.textContent.split('°')[0];
//         console.log(newUserRate);
//         console.log(e.textContent);
//     }

// });
