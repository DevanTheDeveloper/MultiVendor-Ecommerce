

document.addEventListener('DOMContentLoaded',() => {
	const $navbarTags = Array.prototype.slice.call(document.querySelectorAll('.navbagTag'),0);


	if ($navbarTags.length > 0) {
		$navbarTags.forEach( el =>{

			el.addEventListener('click', () => {

				const target = el.dataset.target;
				const $target = document.getElementById(target);

				el.classList.toggle('is-active');
				$target.classList.toggle('is-active');
			});
		});
	}

});