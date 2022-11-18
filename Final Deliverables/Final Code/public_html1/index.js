/* 
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/ClientSide/javascript.js to edit this template
 */


function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  $("#email").text(profile.getEmail());
  $("#pass").text(profile.getPass());
  $(".data").css("display","block");
  $(".g-signin2").css("display","none");
}

 function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
     alert("you have signed out");
     $(".g-signin2").css("display","block");
     $(".data").css("display","none");
    });
  }