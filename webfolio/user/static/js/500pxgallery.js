
var imgHeightAR = [];
var imgWidthAR = [];

function sectionAppear() {
    var galleryGrid = document.getElementById("imgGrid");
    galleryGrid.style.opacity = 1;
}

function gallery_creator(gallery) {
    var arrayOfObjects = gallery;
    var windowAR = window.innerWidth/window.innerHeight+1;
    var galleryGrid = document.getElementById("imgGrid");
    var sectionInfo = galleryGrid.getBoundingClientRect();
    var sectionWidth = sectionInfo.width-17;
    var maxWidthColumn = sectionWidth;
    var maxHeightRow = maxWidthColumn/windowAR;
    var columnMargin = 8;
    var rowMargin = 8;
    var gridHeigth = 0;
    var transX = 0;
    var transX2 = 0;
    var idObject = {};
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

            transX += imageWidth*imageReduction+columnMargin;
            idObject["Im" + i] = iAR;
            gridAR += iARWidth/iARHeight;

            if (gridAR > windowAR || i == arrayOfObjects.length-1) {

                var elInObj = countProperties(idObject);
                finalRowHeight = (maxWidthColumn-((elInObj-1)*columnMargin))/gridAR;
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
                galleryGrid.appendChild(figureGrid);
                img.src = imgPath;
                img.setAttribute("id", "Im" + i);
                img.style.height = maxHeightRow;
                console.log(maxHeightRow);
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
            if(img.complete)
            incrementCounter();
            else
            img.addEventListener( 'load', incrementCounter, false );
        });

        function incrementCounter() {
            counter++;
            if ( counter === len ) {
                figResize();
            }
        }

        function figResize() {
    
            for (i = 0; i < figTarget.length; i++) {
                var fWidth = imgTarget[i].width;
                var fHeight = imgTarget[i].height;
                figTarget[i].style.width = fWidth + "px";
                fdiv1[i].style.width = fWidth + "px";
                fdiv2[i].style.width = fWidth + "px";
                imgWidthAR.push(fWidth/window.innerWidth);
            }
            galleryGrid.style.opacity = 1;
        }
    }
}

/* Esta parte es para recalcular el tamaño de todo al cambiar la pantalla
function galleryNewSize() {
    var actWindowWidth = window.innerWidth;
    for (i = 0; i < imgTarget.length; i++) {
        var newWidth = imgWidthAR[i]*actWindowWidth;
        imgTarget[i].style.width = newWidth + "px";
    }
}

window.addEventListener("resize", galleryNewSize);*/

document.addEventListener("click", function(event){
    var targetElement = event.target || event.srcElement;
    var targetElClass = targetElement.classList;
    console.log(targetElement);
    if (targetElClass.contains("delImg")) {
        var val = targetElement.value;
        tagRem(val, 'image');
        console.log(val);
    }
});
