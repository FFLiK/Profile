window.onload = function(){
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            setAnimation();
            setIconAnimation();
            setBackgroundIconAnimation();
            openclose();
        });
    });
}

function setAnimation() {
    let elements = document.querySelectorAll('.animate');

    let i = 0;
    let n = elements.length;
    for (i; i < n; i++) {
        elements[i].style.opacity = "1.0";
        elements[i].style.transitionDelay = 0.05 * i + "s";
    }
}

function setIconAnimation() {
    let observer = new IntersectionObserver((element) => {
            element[0].target.style.transform = "scale(1.0)";
        }
    )

    let element = document.querySelector('#icon');
    if (element) observer.observe(element);
}

function setBackgroundIconAnimation() {
    let observer = new IntersectionObserver((element) => {
            element[0].target.style.opacity = "0.05";
            element[0].target.style.bottom = "-20%";
        }
    )

    let element = document.querySelector('#background-icon');
    if (element) observer.observe(element);
}

function openclose() {
    const allOpenclose = document.querySelectorAll('.openclose');
    console.log(allOpenclose);
    allOpenclose.forEach(function(openclose) {
        openclose.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href");

            const target = document.querySelector('.' + targetId);
            const targetDisplay = target.style.display;
            if (targetDisplay === 'inline') {
                target.style.display = 'none';
                this.innerHTML = "<small class='clr-tiny' style='text-decoration: underline'>자세히 보기</small>"
            } else {
                target.style.display = 'inline';
                this.innerHTML = "<small class='clr-tiny' style='text-decoration: underline'>접기</small>"
            }
        });
    });
}