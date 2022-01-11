// ==UserScript==
// @name         Fanfiction.net copiable
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Fanfiction blocks selecting story text.  This disables that blocking.
// @author       Jon Heard
// @match        https://www.fanfiction.net/*
// @grant        none
// @require      
// ==/UserScript==

setTimeout(function() {
  const toUnblock = document.getElementById("storytextp");
  toUnblock.style["user-select"] = null;
}, 1000);
