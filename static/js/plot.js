var lineDiv = document.getElementById('line-chart');

var traceA = {
  x: [1, 2, 3, 4, 16, 17, 26],
  y: [1, 40, 9, 60, 4, 20, 10],
  type: 'scatter'
};

var traceB = {
  y: [1, 2, 3, 4, 16, 17, 26],
  x: [1, 40, 9, 60, 4, 20, 10],
  type: 'scatter'
};

var data = [traceA, traceB];

var layout = {
  title:'A Line Chart'
};

Plotly.plot( lineDiv, data, layout );
