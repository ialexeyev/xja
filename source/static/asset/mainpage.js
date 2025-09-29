/* SKILL UP application main page scripts */

window.onload = () => {
    document.body.style.opacity = "1";
}

/*
setInterval(() => {
    console.log('hey');
}, 6000); // Every minute
*/


function divideFullName(fullname) {
  const firstSpaceIndex = fullname.indexOf(" ");
  const firstname = fullname.substring(0, firstSpaceIndex); 
  const lastname = fullname.substring(firstSpaceIndex + 1);
  return [firstname, lastname]
}
