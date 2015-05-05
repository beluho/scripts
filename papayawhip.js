javascript: (function ()
  { Array.prototype.forEach.call(document.querySelectorAll('*'), function(element) { Object.keys(element.style).filter(function(styleName) { return styleName.toLowerCase().indexOf("color") != -1 }).forEach(function(styleName) { element.style[styleName] = 'papayawhip' }); });

  ());
