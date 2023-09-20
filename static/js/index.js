let exploreBtn = document.querySelector('#explore');

exploreBtn.addEventListener('click', function() {
  window.location.href = "chatbot.html";
})

const faqs = document.querySelectorAll(".faq");

faqs.forEach(faq => {
  faq.addEventListener("click", () => {
    for(let faqItem of faqs) {
      if(faqItem == faq){
        faqItem.classList.toggle("active");
      }else{
        faqItem.classList.remove("active");
      }
    }
  })
})
