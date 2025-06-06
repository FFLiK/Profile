window.onload = function(){
    selector();

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            setAnimation();
            setIconAnimation();
            setBackgroundIconAnimation();
            openclose();
        });
    });
}

function selector() {
    const links = document.querySelectorAll(".a-inside");

    fetch(`tools/languages.html`)
        .then(response => response.text())
        .then(data => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, "text/html");
            const targetDiv = doc.querySelector(".tool-division");

            //append targetDiv to body
            document.querySelector(".tools-container").innerHTML = targetDiv.innerHTML;
        })
        .then(() => {
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    setAnimation();
                });
            });
        });

    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href");

            console.log(targetId);

            fetch(`tools/${targetId}.html`)
                .then(response => response.text())
                .then(data => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(data, "text/html");
                    const targetDiv = doc.querySelector(".tool-division");

                    //append targetDiv to body
                    document.querySelector(".tools-container").innerHTML = targetDiv.innerHTML;
                })
                .then(() => {
                    requestAnimationFrame(() => {
                        requestAnimationFrame(() => {
                            setAnimation();
                        });
                    });
                });
        });
    });
}