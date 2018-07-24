$(function(){
  'use strict'

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    ch1.update();
    ch1.update();
  });

  $('#sparkline1').sparkline('html', {
    width: 100,
    height: 30,
    lineColor: '#0083CD',
    fillColor: 'rgba(0,131,205,0.2)',
  });

  $('#sparkline2').sparkline('html', {
    width: 100,
    height: 30,
    lineColor: '#1CAF9A',
    fillColor: 'rgba(28,175,154,0.2)',
  });

  $('#sparkline3').sparkline('html', {
    width: 100,
    height: 30,
    lineColor: '#F49917',
    fillColor: 'rgba(244,153,23,0.2)',
  });

  $('#sparkline4').sparkline('html', {
    width: 100,
    height: 30,
    lineColor: '#ED2475',
    fillColor: 'rgba(237,36,117,0.2)',
  });

  $('#sparkline5').sparkline('html', {
    width: 100,
    height: 30,
    lineColor: '#1CAF9A',
    fillColor: 'rgba(28,175,154,0.2)',
  });


  $('#sparkline6').sparkline('html', {
    type: 'bar',
    barWidth: 5,
    chartRangeMin: 0,
    chartRangeMax: 10,
    width: 100,
    height: 40,
    barColor: '#5E37A6'
  });

  $('#sparkline7').sparkline('html', {
    type: 'bar',
    barWidth: 5,
    chartRangeMin: 0,
    chartRangeMax: 10,
    width: 100,
    height: 40,
    barColor: '#17A2B8'
  });

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    line1.configure({
      width: $('#chartLine1').width(),
      height: $('#chartLine1').height()
    });
    line1.render();
  });

  // peity charts
  $('.peity-line').peity('line');
  $('.peity-donut').peity('donut');

});
