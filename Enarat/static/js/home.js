const loveText = document.getElementById('love-text');
const floatingHeart = document.getElementById('f-h');
const airPlane = document.getElementById('airplane');
var teleport = false
$('.top').on('click', function(){
	$(this).toggleClass('closed');
});
const lovePhrases = [
    "I love you",
    "You're mine",
    "My forever",
    "Only you",
    "You're it",
    "Love wins",
    "I'm yours",
    "My angel",
    "Soulmate",
    "Always us",
    "Be my love",
    "My person",
    "True love",
    "You + me",
    "Infinite",
    "Love grows",
    "Heart full",
    "Love lives",
    "Together",
    "Pure love",
    "Eternal ❤️",
    "All for you",
    "My heart 💕",
    "Endless 💞",
    "XOXO 💋",
    "Sweetheart",
    "Lovebirds",
    "Loving you",
    "Forever ❤️",
    "Amore mio",
    "Love strong",
    "My one ❤️",
    "My world",
    "Love story",
    "Adore you",
    "Love bug 🐞",
    "Crazy love",
    "Kiss me 💋",
    "Love spark",
    "Luv u 4ever",
    "Love life",
    "Love hope",
    "My reason",
    "Hugs & ❤️",
    "Amour fou",
    "Love light",
    "Babe always",
    "I need you",
    "My heart 💘",
    "My always",
    "Luv always",
    "Endless 😍",
    "Love beam",
    "Love blooms",
    "Heart home",
    "Love heals",
    "Aim true ❤️",
    "Love rules",
    "Love bond",
    "Love glow",
    "My darling",
    "Love is all",
    "Love magic",
    "My treasure",
    "Love, me 💕",
    "My lovebug",
    "To infinity",
    "Luv u more",
    "My forever!",
    "Love quest",
    "My reason!",
    "My diamond 💎",
    "Luv 2gether",
    "My beloved",
    "Heart beat",
    "Heart full❤️",
    "Love thrives",
    "Adoring 💖",
    "Love pulse",
    "Moon & back",
    "Soul matter",
    "Love blooms 🌹",
    "Always love",
    "Lovingly 💞",
    "My heartbeat",
    "My one&only",
    "Love sparkles",
    "Love's pure 💗",
    "Kiss always",
    "My heartbeat ❤️",
    "Love grows 🌱",
    "Love's power",
    "Pure joy ❤️",
    "Heart&soul",
    "Forevermore"
  ];

  
let counter = 0;
setInterval(()=>{
    loveText.innerHTML = lovePhrases[counter];
    counter ++;
    if (counter >= lovePhrases.length){
        counter = 0;
    };
},1000);
setInterval(()=>{
    airPlane.style.top =  Math.floor(Math.random() * (70 - 20 + 1)) + 20 + '%';
},15000);


function goToPage(mainPage,page,HB = true){
    if (teleport == false){
    const heartInitiateBox = document.getElementById(`box-${mainPage}-1-ending`);
    if(HB){
        var heartBtn = document.getElementById('heart-btn-'+mainPage)
    }
    const heartBoxWidth = window.getComputedStyle(heartInitiateBox).width
    teleport = true
    floatingHeart.style.left = heartBoxWidth
    let pagePos = parseInt(window.innerHeight)*(mainPage)
    let mainPagePosBottom = 70
    let heartBtnPos = pagePos - 105
    
    let speed = 5;
    let floatingHeartTop = pagePos - 200;
    let floatingHeartOpacity = 0;
    function Flow (){
        {
            floatingHeart.style.opacity = floatingHeartOpacity;
            floatingHeart.style.top  = floatingHeartTop +'px';
            if (floatingHeartTop >= heartBtnPos && HB){
              mainPagePosBottom --;
              clearInterval(floatingHeartInterval)
              speed = .5
              floatingHeartInterval= setInterval(Flow, speed)

              floatingHeartInterval.inte
              heartBtn.style.bottom = (mainPagePosBottom)+'px'
            }
            floatingHeartTop ++;
            floatingHeartOpacity += .005;
            if (floatingHeartTop >= pagePos){
                floatingHeart.style.opacity =0;
                clearInterval(floatingHeartInterval);
                window.scrollTo({
                    top:parseInt(window.innerHeight)*(page-1),
                    behavior:'smooth'
                });
                if(HB){
                heartBtn.style.display ='none'
                setTimeout(()=>{
                  heartBtn.style.bottom = 70 + 'px';
                  heartBtn.style.display='block'
                },500)
            }   
                teleport = false;
            };
        }
    }
    var floatingHeartInterval = setInterval(Flow,speed);
}
    
};

