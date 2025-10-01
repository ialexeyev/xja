/* SKILL UP application main page scripts */

window.onload = () => {
    document.body.style.opacity = "1";
}

function divideFullName(fullname) {
  const firstSpaceIndex = fullname.indexOf(" ");
  const firstname = fullname.substring(0, firstSpaceIndex); 
  const lastname = fullname.substring(firstSpaceIndex + 1);
  return [firstname, lastname]
}
