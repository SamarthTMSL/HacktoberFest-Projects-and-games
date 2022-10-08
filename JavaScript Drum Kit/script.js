const PLAYING_CLASS = 'playing';

const keyToAudioMap = {
  'a' : './sounds/clap.wav',
  's' : './sounds/hihat.wav',
  'd' : './sounds/kick.wav',
  'f' : './sounds/openhat.wav',
  'g' : './sounds/boom.wav',
  'h' : './sounds/ride.wav',
  'j' : './sounds/snare.wav',
  'k' : './sounds/tom.wav',
  'l' : './sounds/tink.wav'
}

document.addEventListener('keydown', (e) => {
  const keyPressed = e.key.toLowerCase();
  if (!keyToAudioMap[keyPressed]) { return false; }
  playRelevantAudio(keyPressed);
  addPlayingClassToBtnElement(keyPressed);
})

function playRelevantAudio(keyPressed) {
  audio = new Audio(keyToAudioMap[keyPressed]);
  audio.play();
}

function addPlayingClassToBtnElement(keyPressed) {
  const btnElement = document.getElementById(`drm-btn-${keyPressed}`);
  btnElement.classList.add(PLAYING_CLASS);
  setTimeout(() => {
    btnElement.classList.remove(PLAYING_CLASS);
  }, 100);
}