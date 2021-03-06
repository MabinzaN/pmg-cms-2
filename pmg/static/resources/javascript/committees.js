var $search = $('#committee-search');
var $searchInput = $('#committee-search input');
var $searchResult = $('.committee-search-result');
var $resultsFound = $('.results-found');
var $noResults = $('.no-results');
var $clearResults = $('.clear-results');
var $committees = $('.committees-list .nat .committee');
var $committeesList = $('.committees-list');
var $committeeNavItem = $('.committee-nav a, .committee-dd-nav a');
var showingSearchResult = false;

var clearSearchResult = function() {
  $searchResult.find('.left ul, .right ul')
    .empty();
  $noResults.hide();
  $resultsFound.hide();
  $committeesList.show();
}

// Underscore debounce
var debounce = function(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

var typeAhead = debounce(function() {
  var value = $searchInput.val();

  clearSearchResult();

  if(!!value.length) {
    var $results = [];
    var resultsCount = 0;

    showingSearchResult = true;

    $committeesList.hide();
    $noResults.hide();
    $clearResults.show();

    $committees.each(function() {
      var $self = $(this);

      if($self.find('a').text().toLowerCase().includes(value.toLowerCase())) {
        $results.push($self.clone());
      }
    });

    resultsCount = $results.length;

    if(!!resultsCount) {
      $resultsFound.show();

      if(resultsCount >= 40) {
        $searchResult.find('.left ul')
          .append($results.slice(0,resultsCount / 2 - 1));
        $searchResult.find('.right ul')
          .append($results.slice(resultsCount,resultsCount - 1))
      } else {
        $searchResult.find('.left ul')
          .append($results);
      }
    } else {
      $resultsFound.hide();
      $noResults.show();
    }
  }
},200);

$committeeNavItem.on('click', function (e) {
  e.preventDefault();
  $(this).tab('show');
  $committees = $('.committees-list .tab-pane.active .committee');

  if(showingSearchResult) clearSearchResult();
});

$searchInput.on('keyup', typeAhead);
