// /* Project specific Javascript goes here. */
// import LazyImage from 'django-lazy-image';

// // Only run the below code if the page has a lazy image instance
// const lazyImage = document.querySelector('.js-LazyImage')
// if (lazyImage) {
//   // Collect all the lazy images on the page
//   const lazyImages = document.querySelectorAll('.js-LazyImage')
//   // Set up our IntersectionObserver callback
//   const callback = (entries, observer) => {
//     Array.from(entries).forEach((entry, index) => {
//       // If any of the images have come in to view, activate them sequentially
//       if (entry.isIntersecting && !entry.target.dataset.activating) {
//         entry.target.dataset.activating = true
//         window.setTimeout(() => {
//           new LazyImage({ el: entry.target })
//           observer.unobserve(entry.target)
//         }, 150 * index)
//       }
//     })
//   }
//   const observer = new IntersectionObserver(callback, {
//     threshold: 0.4
//   })
//   Array.from(lazyImages).forEach(image => observer.observe(image))
// }