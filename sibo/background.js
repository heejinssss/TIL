let audio;

chrome.runtime.onStartup.addListener(() => {
  audio = new Audio("C:\Users\Owner\Desktop\sibo\cock-a-doodle-doo.wav");
});

chrome.alarms.create("hourly-reminder", {
  delayInMinutes: 60,
  periodInMinutes: 60
});

chrome.alarms.onAlarm.addListener(alarm => {
  if (alarm.name === "hourly-reminder") {
    const options = {
      type: "basic",
      iconUrl: "icon.png",
      title: "Hourly Reminder with Bae",
      message: "어느새 1시간이 지났네요. 일은 잘 되어 가시나요?."
    };
    chrome.notifications.create(options);
    if (audio) {
      audio.play();
    }
  }
});