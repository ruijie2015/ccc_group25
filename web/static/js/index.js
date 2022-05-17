var suburb_list, school_num, tweet_num;
var myChart_l1, option_l1;

// chart: left 1 
(function () {
  $.ajax({
    url: "/l1",
    async: false,
    success: function (data) {
      //console.log(data);
      suburb_list = data.suburb;
      school_num = data.school_num;
      tweet_num = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  myChart_l1 = echarts.init(document.querySelector(".bar .chart"));
  option_l1 = {
    color: ["#2f89cf", "#73c0de"],
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow"
      }
    },
    grid: {
      left: "0%",
      top: "25px",
      right: "0%",
      bottom: "0%",
      containLabel: true
    },
    xAxis: [
      {
        type: "category",
        data: suburb_list,
        axisTick: {
          alignWithLabel: true
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          show: false
        }
      }
    ],
    yAxis: [
      {
        type: "value",
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    legend: {
      textStyle: {
        color: "#4c9bfd"
      }
    },
    series: [
      {
        name: 'Tweets num',
        type: 'bar',
        emphasis: {
          focus: 'series'
        },
        barWidth: "15%",
        itemStyle: {
          barBorderRadius: 5
        },
        data: tweet_num
      },
      {
        name: 'School num',
        type: 'bar',
        emphasis: {
          focus: 'series'
        },
        barWidth: "15%",
        itemStyle: {
          barBorderRadius: 5
        },
        data: school_num
      },
    ]
  };

  myChart_l1.setOption(option_l1);
  window.addEventListener("resize", function () {
    myChart_l1.resize();
  });

})();

function chart_l1() {
  $.ajax({
    url: "/l1",
    success: function (data) {
      console.log(data);
      suburb_list = data.suburb;
      school_num = data.school_num;
      tweet_num = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  var dataAll = [
    { year: "Tweets num", data: tweet_num },
    { year: "School num", data: school_num }
  ];

  option_l1.series[0].data = dataAll[0].data;
  option_l1.series[1].data = dataAll[1].data;
  myChart_l1.setOption(option_l1);
}
setInterval("chart_l1()", 3000);


var tweet_num_year, school_num_year, enroll_num_year;
var myChart_l2, option_l2;
// chart: left 2
(function () {
  $.ajax({
    url: "/l2",
    async: false,
    success: function (data) {
      //console.log(data);
      enroll_num_year = data.enroll_num;
      school_num_year = data.school_num;
      tweet_num_year = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  myChart_l2 = echarts.init(document.querySelector(".line .chart"));

  var data = {
    year: [
      enroll_num_year, school_num_year, tweet_num_year
    ]
  };

  option_l2 = {
    color: ["#00f2f1", "#ed3f35", "#4c9bfd"],
    tooltip: {
      trigger: "axis"
    },
    legend: {
      right: "10%",
      textStyle: {
        color: "#4c9bfd"
      }
    },
    grid: {
      top: "15%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: [
        "2014",
        "2015",
        "2016",
        "2017"
      ],
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [
      {
        name: "enroll num",
        type: "line",
        smooth: true,
        data: data.year[0]
      },
      {
        name: "school num",
        type: "line",
        smooth: true,
        data: data.year[1]
      },
      {
        name: "tweets num",
        type: "line",
        smooth: true,
        data: data.year[2]
      },
    ]
  };
  myChart_l2.setOption(option_l2);
  window.addEventListener("resize", function () {
    myChart_l2.resize();
  });
})();

//function chart_l2() {
//  $.ajax({
//    url: "/l2",
//    success: function (data) {
//      //console.log(data);
//      enroll_num_year = data.enroll_num;
//      school_num_year = data.school_num;
//      tweet_num_year = data.tweet_num;
//    },
//    error: function () {
//      alert("ajax request failed")
//    }
//  });
//
//  option_l2.series[0].data = enroll_num_year;
//  option_l2.series[1].data = school_num_year;
//  option_l2.series[2].data = tweet_num_year;
//  myChart_l2.setOption(option_l2);
//}
//setInterval("chart_l2()", 3000);


var keyword, keyword_num;
var myChart_l3, option_l3;
// chart: left 3
(function () {
  $.ajax({
    url: "/l3",
    async: false,
    success: function (data) {
      //console.log(data);
      keyword = data.words;
      keyword_num = data.word_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  myChart_l3 = echarts.init(document.querySelector(".pie .chart"));

  option_l3 = {
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
      position: function (p) {
        return [p[0] + 10, p[1] - 10];
      }
    },
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      data: keyword,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    series: [
      {
        name: "keyword",
        type: "pie",
        center: ["50%", "42%"],
        radius: ["40%", "60%"],
        color: [
          "#065aab",
          "#066eab",
          "#0682ab",
          "#0696ab",
          "#06a0ab",
          "#06b4ab",
          "#06c8ab",
          "#06dcab",
          "#06f0ab"
        ],
        label: { show: false },
        labelLine: { show: false },
        data: [
          { value: keyword_num[0], name: keyword[0] },
          { value: keyword_num[1], name: keyword[1] },
          { value: keyword_num[2], name: keyword[2] },
          { value: keyword_num[3], name: keyword[3] },
          { value: keyword_num[4], name: keyword[4] },
          { value: keyword_num[5], name: keyword[5] },
        ]
      }
    ]
  };

  myChart_l3.setOption(option_l3);
  window.addEventListener("resize", function () {
    myChart_l3.resize();
  });
})();

function chart_l3() {
  $.ajax({
    url: "/l3",
    success: function (data) {
      //console.log(data);
      keyword = data.words;
      keyword_num = data.word_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  option_l3.series[0].data[0].value = keyword_num[0];
  option_l3.series[0].data[1].value = keyword_num[1];
  option_l3.series[0].data[2].value = keyword_num[2];
  option_l3.series[0].data[3].value = keyword_num[3];
  option_l3.series[0].data[4].value = keyword_num[4];
  option_l3.series[0].data[5].value = keyword_num[5];
  myChart_l3.setOption(option_l3);
}
setInterval("chart_l3()", 3000);


var suburb_r1, tweet_r1;
var myChart_r1, option_r1;
// chart: right 1
(function () {
  $.ajax({
    url: "/r1",
    async: false,
    success: function (data) {
      //console.log(data);
      suburb_r1 = data.suburb;
      tweet_r1 = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });
  myChart_r1 = echarts.init(document.querySelector(".bar1 .chart"));

  var data = [0, 0, 0, 0, 0];
  var total = tweet_r1[0] + tweet_r1[1] + tweet_r1[2] + tweet_r1[3] + tweet_r1[4];
  for (var i = 0; i < data.length; i++) {
    data[i] = Math.round(tweet_r1[i] * 100 / total);
  }


  var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
  option_r1 = {
    grid: {
      top: "10%",
      left: "30%",
      bottom: "10%"
    },
    xAxis: {
      show: false
    },
    yAxis: [
      {
        show: true,
        data: suburb_r1,
        inverse: true,
        axisLine: {
          show: false
        },
        splitLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        axisLabel: {
          color: "#fff",

          rich: {
            lg: {
              backgroundColor: "#339911",
              color: "#fff",
              borderRadius: 15,
              // padding: 5,
              align: "center",
              width: 15,
              height: 15
            }
          }
        }
      },
      {
        show: true,
        inverse: true,
        data: tweet_r1,
        axisLabel: {
          textStyle: {
            fontSize: 12,
            color: "#fff"
          }
        }
      }
    ],
    series: [
      {
        name: "条",
        type: "bar",
        yAxisIndex: 0,
        data: data,
        barCategoryGap: 50,
        barWidth: 10,
        itemStyle: {
          normal: {
            barBorderRadius: 20,
            color: function (params) {
              var num = myColor.length;
              return myColor[params.dataIndex % num];
            }
          }
        },
        label: {
          normal: {
            show: true,
            position: "inside",
            formatter: "{c}%"
          }
        }
      },
      {
        name: "框",
        type: "bar",
        yAxisIndex: 1,
        barCategoryGap: 50,
        data: [100, 100, 100, 100, 100],
        barWidth: 15,
        itemStyle: {
          normal: {
            color: "none",
            borderColor: "#00c1de",
            borderWidth: 3,
            barBorderRadius: 15
          }
        }
      }
    ]
  };

  myChart_r1.setOption(option_r1);
  window.addEventListener("resize", function () {
    myChart_r1.resize();
  });
})();

function chart_r1() {
  $.ajax({
    url: "/r1",
    success: function (data) {
      //console.log(data);
      suburb_r1 = data.suburb;
      tweet_r1 = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });
  var data = [0, 0, 0, 0, 0];
  var titlename = suburb_r1;
  var total = tweet_r1[0] + tweet_r1[1] + tweet_r1[2] + tweet_r1[3] + tweet_r1[4];
  for (var i = 0; i < data.length; i++) {
    data[i] = Math.round(tweet_r1[i] * 100 / total);
  }
  console.log(data);
  option_r1.yAxis[0].data = suburb_r1;
  option_r1.yAxis[1].data = tweet_r1;
  option_r1.series[0].data = data;
  myChart_r1.setOption(option_r1);
}
setInterval("chart_r1()", 3000);



var tweet_r2, bin_num_year, res_num_year;
var myChart_r2, option_r2;
// chart: right 2
(function () {
  $.ajax({
    url: "/r2",
    async: false,
    success: function (data) {
      //console.log(data);
      bin_num_year = data.bin;
      res_num_year = data.residential;
      tweet_r2 = data.tweet_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  myChart_r2 = echarts.init(document.querySelector(".line1 .chart"));

  var data = {
    year: [
      bin_num_year, res_num_year, tweet_r2
    ]
  };

  option_r2 = {
    color: ["#00f2f1", "#ed3f35", "#4c9bfd"],
    tooltip: {
      trigger: "axis"
    },
    legend: {
      right: "10%",
      textStyle: {
        color: "#4c9bfd"
      }
    },
    grid: {
      top: "15%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: [
        "2014",
        "2015",
        "2016",
        "2017"
      ],
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [
      {
        name: "bin num",
        type: "line",
        smooth: true,
        data: data.year[0]
      },
      {
        name: "residential num",
        type: "line",
        smooth: true,
        data: data.year[1]
      },
      {
        name: "tweets num",
        type: "line",
        smooth: true,
        data: data.year[2]
      },
    ]
  };
  myChart_r2.setOption(option_r2);
  window.addEventListener("resize", function () {
    myChart_r2.resize();
  });
})();

//function chart_r2() {
//  $.ajax({
//    url: "/r2",
//    success: function (data) {
//      //console.log(data);
//      bin_num_year = data.bin;
//      res_num_year = data.residential;
//      tweet_r2 = data.tweet_num;
//    },
//    error: function () {
//      alert("ajax request failed")
//    }
//  });
//
//  option_r2.series[0].data = bin_num_year;
//  option_r2.series[1].data = res_num_year;
//  option_r2.series[2].data = tweet_r2;
//  myChart_r2.setOption(option_r2);
//}
//setInterval("chart_r2()", 3000);


var keyword_r3, keyword_num_r3;
var myChart_r3, option_r3;

// charr: right 3
(function () {
  $.ajax({
    url: "/r3",
    async: false,
    success: function (data) {
      //console.log(data);
      keyword_r3 = data.words;
      keyword_num_r3 = data.word_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  myChart_r3 = echarts.init(document.querySelector(".pie1  .chart"));
  option_r3 = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "keyword",
        type: "pie",
        radius: ["10%", "60%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: [
          { value: keyword_num_r3[0], name: keyword_r3[0] },
          { value: keyword_num_r3[1], name: keyword_r3[1] },
          { value: keyword_num_r3[2], name: keyword_r3[2] },
          { value: keyword_num_r3[3], name: keyword_r3[3] },
          { value: keyword_num_r3[4], name: keyword_r3[4] },
          { value: keyword_num_r3[5], name: keyword_r3[5] },
          { value: keyword_num_r3[6], name: keyword_r3[6] },
          { value: keyword_num_r3[7], name: keyword_r3[7] }
        ],
        label: {
          fontSize: 10
        },
        labelLine: {
          // from shape
          length: 5,
          // from text
          length2: 10
        }
      }
    ]
  };
  myChart_r3.setOption(option_r3);
  window.addEventListener("resize", function () {
    myChart_r3.resize();
  });
})();

function chart_r3() {
  $.ajax({
    url: "/r3",
    success: function (data) {
      //console.log(data);
      keyword_r3 = data.words;
      keyword_num_r3 = data.word_num;
    },
    error: function () {
      alert("ajax request failed")
    }
  });

  option_r3.series[0].data[0].value = keyword_num_r3[0];
  option_r3.series[0].data[0].name = keyword_r3[0];
  option_r3.series[0].data[1].value = keyword_num_r3[1];
  option_r3.series[0].data[1].name = keyword_r3[1];
  option_r3.series[0].data[2].value = keyword_num_r3[2];
  option_r3.series[0].data[2].name = keyword_r3[2];
  option_r3.series[0].data[3].value = keyword_num_r3[3];
  option_r3.series[0].data[3].name = keyword_r3[3];
  option_r3.series[0].data[4].value = keyword_num_r3[4];
  option_r3.series[0].data[4].name = keyword_r3[4];
  option_r3.series[0].data[5].value = keyword_num_r3[5];
  option_r3.series[0].data[5].name = keyword_r3[5];
  option_r3.series[0].data[6].value = keyword_num_r3[6];
  option_r3.series[0].data[6].name = keyword_r3[6];
  option_r3.series[0].data[7].value = keyword_num_r3[7];
  option_r3.series[0].data[7].name = keyword_r3[7];
  myChart_r3.setOption(option_r3);
}
setInterval("chart_r3()", 3000);

