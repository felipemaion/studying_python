Packt.dotdclock = {
	init: function () {
		if (!$('#deal-of-the-day').length) {
			return false;
		}
		var utcOffset = ($('div#dotd-clock').attr("data-time-offset")) * 1000;
		Packt.dotdclock.countdown(utcOffset);
		setInterval(function () {
			var utcOffset = ($('div#dotd-clock').attr("data-time-offset")) * 1000;
			Packt.dotdclock.countdown(utcOffset);
		}, 1000);
	},
	countdown: function (utcOffset) {
		var now = new Date();
		var h = (now.getUTCHours() * 3600000);
		var m = (now.getUTCMinutes() * 60000);
		var s = (now.getUTCSeconds() * 1000);
		var timeLeft = 86400000 - (h + m + s) - utcOffset;
		var milliseconds = parseInt((timeLeft % 1000) / 100),
			seconds = parseInt((timeLeft / 1000) % 60),
			minutes = parseInt((timeLeft / (1000 * 60)) % 60),
			hours = parseInt((timeLeft / (1000 * 60 * 60)) % 24);
		hours = (hours < 10) ? "0" + hours : hours;
		minutes = (minutes < 10) ? "0" + minutes : minutes;
		seconds = (seconds < 10) ? "0" + seconds : seconds;
		$('#dotd-clock').html(hours + ":" + minutes + ":" + seconds);
	}
}








var utcOffset = "1538002800" * 1000;
function countdown (utcOffset) {
	var now = new Date();
	var h = (now.getUTCHours() * 3600000);
	var m = (now.getUTCMinutes() * 60000);
	var s = (now.getUTCSeconds() * 1000);
	var timeLeft = 86400000 - (h + m + s) - utcOffset;
	alert(timeLeft);
	var milliseconds = parseInt((timeLeft % 1000) / 100),
		seconds = parseInt((timeLeft / 1000) % 60),
		minutes = parseInt((timeLeft / (1000 * 60)) % 60),
		hours = parseInt((timeLeft / (1000 * 60 * 60)) % 24);
		alert(hours);
	// hours = (hours < 10) ? "0" + hours : hours;
	// minutes = (minutes < 10) ? "0" + minutes : minutes;
	// seconds = (seconds < 10) ? "0" + seconds : seconds;
	alert(hours + ":" + minutes + ":" + seconds);
}

countdown (utcOffset);