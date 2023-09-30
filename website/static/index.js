
function deleteNote(noteId) {
  let nid = noteId;
  let index = nid.indexOf(".com") + 4;
  let email = nid.slice(0,index);
  let s = "/home/";
  let result = s.concat(email);

  // sending a request to '/delete-note'
  // then reloading the window (home page)
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = result;
  });
}  

function deleteImage(url) {
  let index = url.indexOf(".com") + 4;
  let email = url.slice(0,index);
  let s = url.slice(index);
  index = s.indexOf(".net") + 5;
  let name = s.slice(index);
  let a = "/home/";
  let result = a.concat(email);

  fetch("/delete-image", {
    method: "POST",
    body: JSON.stringify({ email: email, name: name }),
  }).then((_res) => {
    window.location.href = result;
  });
}

function shareNote(info) {

  let index = info.indexOf(":");
  let title = info.slice(0,index);
  let button = info.slice(index+1);
  let address = encodeURI(document.location.href);
  let result;

  switch(button) {
    case "facebook":
      result = `https://www.facebook.com/sharer.php?u=${address}`;
      break;
    case "twitter":
      result = `https://twitter.com/share?url=${address}&text=${title}`;
      break;
    case "linkedin":
      result = `https://www.linkedin.com/sharing/share-offsite/?url=${address}`;
      break;
    case "whatsapp":
      result = `https://wa.me/?text=${title} ${address}`;
      break;
  }

  window.open(
    result,
    '_blank' 
  );
}

