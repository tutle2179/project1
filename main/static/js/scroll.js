const progressTag = document.querySelector('.progress')
const progressText = document.querySelector('p')
const bodyTag = document.querySelector('body')

document.addEventListener('scroll', () => {
  const pixels = window.pageYOffset
  const pageHeight = bodyTag.getBoundingClientRect().height
  const totalHeight = pageHeight - window.innerHeight
  const percentage = pixels / totalHeight
  
  progressTag.style.width = `${100 * percentage}%`
  
  if (pixels > 0) {
    progressText.innerHTML = `${Math.floor(100 * percentage)}` + '%'
  } 
  
  else {
    progressText.innerHTML = ''
  }
})
