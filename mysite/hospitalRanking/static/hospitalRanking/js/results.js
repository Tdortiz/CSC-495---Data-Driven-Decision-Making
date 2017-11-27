"use strict";
var hue_red = 0;
var hue_green = 94;

$(function () {

});

/**
 * Shorthand for creating a new circle progress bar.
 *
 * @param id         the id of the container to create the semi-circle in
 * @param percentage the percentage to fill to
 */
function createCircleProgressBar(id, percentage) {
    if( !$(id).length ) return;

    var bar = new ProgressBar.Circle(id, {
        strokeWidth: 10,
        color: '#FFEA82',
        trailColor: '#e0e0e0',
        trailWidth: 6,
        easing: 'easeOut',
        duration: 2000,
        svgStyle: {width: '100%', height: '100%'},

        step: function (state, bar) {
            var value = Math.round(bar.value() * 100);
            bar.color = getHue(bar.value(), hue_red, hue_green);
            bar.path.setAttribute('stroke', bar.color);
            bar.setText(value + "%");
        }
    });

    bar.text.style.color = "#2c2c2c";
    bar.animate(percentage);  // Number from 0.0 to 1.0
}


/**
 * Given a percentage, map that value between the two hues.
 *
 * For exmaple if hue0 is red and hue1 is green a percentage of .75
 * will return a hue that is 75% of the way between red and green.
 *
 * @param percentage between hue0 and hue1
 * @param hue0
 * @param hue1
 * @returns {string} HSV color object
 */
function getHue(percentage, hue0, hue1) {
    var hue = (percentage * (hue1 - hue0)) + hue0;
    return 'hsl(' + hue + ', 70%, 50%)';
}