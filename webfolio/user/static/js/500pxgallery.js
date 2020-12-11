
var imgHeightAR = [];
var imgWidthAR = [];
var imgInfoAR = [];
var imgsWidht = [];
var imgsHeight = [];
var columnMargin = 8;
var rowMargin = 8;
var newGridW = 0;
var nTransX = [];

function sectionAppear() {
    var galleryGrid = document.getElementById("imgGrid");
    galleryGrid.style.opacity = 1;
}

function gallery_creator(gallery) {
    var arrayOfObjects = gallery;
    var windowAR = window.innerWidth/window.innerHeight+1;
    var galleryGrid = document.getElementById("imgGrid");
    var sectionInfo = galleryGrid.getBoundingClientRect();
    var sectionWidth = sectionInfo.width;
    var maxWidthColumn = sectionWidth;
    var maxHeightRow = maxWidthColumn/windowAR;
    var gridHeigth = 0;
    var transX = 0;
    var transX2 = 0;
    var idObject = [];
    var gridAR = 0;
    var finalRowHeight = 0;
    var totalHeightSection = 0;
    
    orderGallery();

    function gcd(a, b) {
        if (b == 0)
          return a;
        else
          return gcd(b, (a % b));
    }

    function countProperties(obj) {
        var count = 0;
        for(var prop in obj) {
            if(obj.hasOwnProperty(prop))
                ++count;
        }
        return count;
    }

    function orderGallery() {
        for (var i = 0; i < arrayOfObjects.length; i++) {
            var image = arrayOfObjects[i];
            var imgPath = "/media/" + image.image_file;
            var img = document.createElement("img");
            var figureGrid = document.createElement("figure");
            var div1 = document.createElement("div");
            var div2 = document.createElement("div");
            var remButton = document.createElement("button");
            var icBut = document.createElement("i");
            var imageWidth = image.width;
            var imageHeight = image.height;
            var imageReduction = maxHeightRow/imageHeight;
            var imageGdc = gcd(imageWidth, imageHeight);
            var iARWidth = imageWidth/imageGdc;
            var iARHeight = imageHeight/imageGdc;
            var iAR = iARWidth + "/" + iARHeight;
            
            gallerySize();

            if (imageWidth > "400"){
                transX += 400/imageGdc;
            } else {
                transX += imageWidth*imageReduction+columnMargin;
            }
            idObject["Im" + i] = iAR;
            imgInfoAR["Im" + i] = iAR;
            gridAR += iARWidth/iARHeight;

            if (gridAR > windowAR || i == arrayOfObjects.length-1) {

                var elInObj = countProperties(idObject);
                finalRowHeight = (maxWidthColumn-((elInObj-1)*columnMargin))/gridAR;
                if (finalRowHeight > 400) {
                    finalRowHeight = 400;
                }
                totalHeightSection += finalRowHeight;
                galleryGrid.style.height = totalHeightSection+maxHeightRow + "px";

                gallerySize();

                for (var key in idObject) {
                    var fImg = document.getElementById(key);
                    fImg.setAttribute("height", finalRowHeight);
                    var parent = fImg.parentElement;
                    parent.style.transform = "translate3d(" + transX2 + "px, " + gridHeigth + "px, 0px)";
                    parent.style.height = finalRowHeight + "px";
                    var idStr = idObject[key];
                    var idSplit = idStr.split("/");
                    var idIntW = idSplit[0];
                    var idIntH = idSplit[1];
                    transX2 += finalRowHeight*idIntW/idIntH+columnMargin;
                }

                transX = 0;
                gridHeigth += finalRowHeight+rowMargin;
                transX2 = 0;
                gridAR = 0;
                idObject = [];
            }

            function gallerySize() {
                figureGrid.style.transform = "translate3d(" + transX + "px, " + gridHeigth + "px, 0px)";
                figureGrid.classList.add("pig-figure");
                figureGrid.height = maxHeightRow;
                galleryGrid.appendChild(figureGrid);
                img.src = imgPath;
                img.setAttribute("id", "Im" + i);
                img.height = maxHeightRow;
                figureGrid.appendChild(img);
                div1.classList.add("pig-div");
                figureGrid.appendChild(div1);
                div2.classList.add("gip-div");
                figureGrid.appendChild(div2);
                remButton.value = (image.id + "," + image.name);
                remButton.classList.add("delImg");
                div1.appendChild(remButton);
                icBut.classList.add("material-icons");
                icBut.classList.add("delImg");
                icBut.innerHTML = "delete_outline";
                remButton.appendChild(icBut);
            }
        }
        imgTarget = document.getElementById('imgGrid').getElementsByTagName("img");
        figTarget = document.getElementById('imgGrid').getElementsByTagName("figure");
        fdiv1 = document.querySelectorAll(".pig-div");
        fdiv2 = document.querySelectorAll(".gip-div");
        var imgs = document.images,
        len = imgs.length,
        counter = 0;

        [].forEach.call( imgs, function( img ) {
            if(img.complete) {
                incrementCounter();
            } else {
                img.addEventListener( 'load', incrementCounter, false );
            }
        });

        function incrementCounter() {
            counter++;
            if ( counter === len ) {
                figResize();
                hideLoader();
            }
        }

        function figResize() {
    
            for (i = 0; i < figTarget.length; i++) {
                var fWidth = imgTarget[i].width;
                var fHeight = imgTarget[i].height;
                figTarget[i].style.width = fWidth + "px";
                fdiv1[i].style.width = fWidth + "px";
                fdiv2[i].style.width = fWidth + "px";
                imgsWidht.push(fWidth);
                imgsHeight.push(fHeight);
                imgWidthAR.push(fWidth/window.innerWidth);
                imgHeightAR.push(fHeight/window.innerHeight);
            }
        }
        function hideLoader() {
            document.getElementById("outainer").style.opacity = 0;
            setTimeout(none, 2000)
            function none() {
                galleryGrid.style.opacity = 1;
                document.getElementById("outainer").style.display = "none";
            }
        }
    }
}

/* Esta parte es para recalcular el tamaño de todo al cambiar la pantalla*/

window.addEventListener("resize", galleryNewSize);
function galleryNewSize() {
    var actWindowWidth = window.innerWidth;
    var imgs = document.images;
    for (i = 0; i < imgs.length; i++) {
        console.log(i);
        var newWidth = imgWidthAR[i]*actWindowWidth;
        var imgID = imgs[i].id;
        var imgAR = imgInfoAR[imgID];
        var imgSplit = imgAR.split("/");
        var imgIntW = imgSplit[0];
        var imgIntH = imgSplit[1];
        var newHeight = newWidth*imgIntH/imgIntW;
        var fig = imgs[i].parentElement;
        var div1 = fig.querySelector(".pig-div");
        var div2 = fig.querySelector(".gip-div");
        var newGridH = newHeight+rowMargin;
        const {x, y, z} = getTranslateValues(fig);


        console.log("x " + x + " ,y " + y);

        imgs[i].style.width = newWidth + "px";
        imgs[i].style.height = newHeight + "px";
        fig.style.width = newWidth + "px";
        fig.style.height = newHeight + "px";
        div1.style.width = newWidth + "px";
        div2.style.width = newWidth + "px";
        console.log("nWidth " + newGridW);
        if (x == 0 && y == 0) {
            newGridW = 0;
            nTransX = [];
            newGridW += newWidth+columnMargin;
            nTransX.push(newGridW);
        }
        if (x != 0 && y == 0) {
            newGridW += newWidth+columnMargin;
            nTransX.push(newGridW);
            fig.style.transform = "translate3d(" + nTransX[i-1] + "px, 0px, 0px)";
        }
        if (x == 0 && y != 0) {
            console.log("Fila nueva");
            newGridW = 0;
            nTransX = [];
            newGridW += newWidth+columnMargin;
            nTransX.push(newGridW);
        }
        if (x != 0 && y != 0) {
            newGridW += newWidth+columnMargin;
            nTransX.push(newGridW);
            fig.style.transform = "translate3d(" + nTransX[i-1] + "px, 0px, 0px)";
        }
        /*fig.style.transform = "translate3d(" + transX + "px, " + newGridH + "px, 0px)";*/
    }
}
function getTranslateValues (element) {
    const style = window.getComputedStyle(element)
    const matrix = style['transform'] || style.webkitTransform || style.mozTransform
    if (matrix === 'none') {
        return {
            x: 0,
            y: 0,
            z: 0
        }
    }
    const matrixType = matrix.includes('3d') ? '3d' : '2d'
    const matrixValues = matrix.match(/matrix.*\((.+)\)/)[1].split(', ')
    if (matrixType === '2d') {
        return {
            x: matrixValues[4],
            y: matrixValues[5],
            z: 0
        }
    }
    if (matrixType === '3d') {
        return {
            x: matrixValues[12],
            y: matrixValues[13],
            z: matrixValues[14]
        }
    }
}

document.addEventListener("click", function(event){
    var targetElement = event.target || event.srcElement;
    var targetElClass = targetElement.classList;
    if (targetElClass.contains("delImg")) {
        var val = targetElement.value;
        tagRem(val, 'image');
    }
});
