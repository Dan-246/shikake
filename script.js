var totalTime = 15000;
var oldTime = Date.now();

var timeId = setInterval(() => {
  var currentTime = Date.now();

  // 差分を求める
  var diff = currentTime - oldTime;
  var diffSec = totalTime - diff;

  //ミリ秒を整数に変換
  var remainSec = diffSec / 1000;

  var text = (remainSec+"0").slice(0,5) + "s";
  
  // 0秒以下になったら
  if (diffSec <= 0) {
    clearInterval(timeId);
    // タイマー終了の文言を表示する
    text = "Game Over";
  }

  // 画面に表示する
  document.querySelector('.timer').innerHTML = text;
})
setTimeout(function(){
  window.location.href = 'https://dan-246.github.io/shikake2/';
}, 19*1000)
