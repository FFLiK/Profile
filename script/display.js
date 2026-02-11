window.onload = function(){
    displayProject();
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            setAnimation();
            setIconAnimation();
            setBackgroundIconAnimation();
            openclose();
        });
    });
}

function displayProject() {
    const params = new URLSearchParams(window.location.search);
    const project = params.get("proj");

    //read json file
    fetch("projects.json")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const projectData = data[project];
            if (!projectData) {
                throw new Error(`Project '${project}' not found`);
            }
            
            const projectTitle = projectData.title;
            const projectDescription = projectData.description;
            const projectType = projectData.type;
            const projectResource = projectData.res;

            //display project
            document.querySelector(".display-title").innerHTML = projectTitle;
            document.querySelector(".display-description").innerHTML = projectDescription;
            console.log(projectType);
            if (projectType === "img") {
                document.querySelector(".display-img").style.display = "block";
                document.querySelector(".display-vid").style.display = "none";
                document.querySelector(".display-pdf").style.display = "none";
                document.querySelector(".display-img").src = "https://assets.profile.fflik.kr/" + projectResource;
            } else if (projectType === "vid") {
                document.querySelector(".display-img").style.display = "none";
                document.querySelector(".display-vid").style.display = "block";
                document.querySelector(".display-pdf").style.display = "none";
                document.querySelector(".display-vid-src").src = "https://assets.profile.fflik.kr/" + projectResource;
                document.querySelector(".display-vid").load();
            } else if (projectType === "pdf") {
                document.querySelector(".display-img").style.display = "none";
                document.querySelector(".display-vid").style.display = "none";
                document.querySelector(".display-pdf").style.display = "block";
                document.querySelector(".display-pdf").src = "https://assets.profile.fflik.kr/" + projectResource;
            } else {
                document.querySelector(".display-img").style.display = "none";
                document.querySelector(".display-vid").style.display = "none";
                document.querySelector(".display-pdf").style.display = "none";
            }
        })
        .then(() => {
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    setAnimation();
                    openclose();
                });
            });
        })
        .catch(error => {
            console.error('Error loading project:', error);
            document.querySelector(".display-title").innerHTML = "오류 발생";
            document.querySelector(".display-description").innerHTML = "프로젝트를 불러올 수 없습니다. 나중에 다시 시도해주세요.";
        });
}