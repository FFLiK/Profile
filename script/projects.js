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

    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href");

            console.log(targetId);

            fetch(`projects/${targetId}.html`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.text();
                })
                .then(data => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(data, "text/html");
                    const targetDiv = doc.querySelector(".project-division");

                    if (!targetDiv) {
                        throw new Error("Project content not found");
                    }

                    //append targetDiv to body
                    document.querySelector(".projects-container").innerHTML = targetDiv.innerHTML;
                })
                .then(() => {
                    requestAnimationFrame(() => {
                        requestAnimationFrame(() => {
                            setAnimation();
                            openclose();
                            document.querySelector(".project-section-name").innerHTML = this.innerHTML;
                        });
                    });
                })
                .catch(error => {
                    console.error('Error loading project:', error);
                    document.querySelector(".projects-container").innerHTML = `
                        <div class="project-box">
                            <div class="project-description-box">
                                <h4>로드 중 오류</h4>
                                <p>프로젝트를 불러올 수 없습니다. 나중에 다시 시도해주세요.</p>
                            </div>
                        </div>
                    `;
                });
        });
    });
}