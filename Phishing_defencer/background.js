chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    chrome.tabs.create({url: request.url}, function(tab) {
      chrome.tabs.executeScript(tab.id, {
        code: 'var links = [];' +
              'var linkList = document.getElementsByTagName("a");' +
              'for (var i = 0; i < linkList.length; i++) {' +
              '  var link = linkList[i];' +
              '  if (link.href) {' +
              '    links.push(link.href);' +
              '  }' +
              '}' +
              'links;'
      }, function(result) {
        sendResponse(result);
        chrome.tabs.remove(tab.id);
      });
    });
    return true;
  });
  