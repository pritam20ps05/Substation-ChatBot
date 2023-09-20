var messages = [];
var temp = 0.5;
var chatmsg_div = document.getElementById("chat-body");

function scrolldownchat() {
  $("#chat-body").animate({ scrollTop: chatmsg_div.scrollHeight }, 1000);
}

function showChatLoading() {
  $("#chat-body").append(
    '<div class="chat-msg-box chat-loading chat-loading-typing"><div class="chat-icon"><img src="' +
      bot_img +
      '" alt="chat-icon" /></div><div class="chat-content"><p class="role">Chatbot</p><div class="chat-msg"><img src="' +
      loading_gif +
      '" alt=""></div></div></div>'
  );
  setTimeout(() => {
    $(".chat-loading-typing").addClass("loading");
  }, 300);
}

function hideChatLoading() {
  $(".chat-loading-typing").addClass("d-none");
  $(".chat-loading-typing").remove();
}

$(document).ready(() => {
  $("#msg-form").on("submit", (e) => {
    e.preventDefault();

    var text = $("#msg-text").val().trim();
    $("#msg-text").val("");
    if (text === "") {
      return;
    }

    // Adding cooldown to text sending
    $("#msg-text").prop("disabled", true);
    setTimeout(() => {
      $("#msg-text").prop("disabled", false);
    }, 15000);

    if (
      Math.floor(chatmsg_div.scrollTop + chatmsg_div.clientHeight) + 50 >
      chatmsg_div.scrollHeight
    ) {
      setTimeout(scrolldownchat, 500);
    }

    $("#chat-body").append(
      '<div class="user-msg-box"><div class="user-content"><p class="role">You</p><div class="user-msg">' +
        text +
        '</div></div><div class="user-icon"><img src="' +
        user_img +
        '" alt="usericon" /></div></div>'
    );
    showChatLoading();

    messages.push({ role: "user", content: text });
    console.log(messages);

    $.ajax({
      method: "POST",
      url: "/api/chatbot",
      data: JSON.stringify({
        messages: messages,
        temp: temp,
      }),
      contentType: "application/json",
      dataType: "json",
    }).done((msg) => {
      messages.push({ role: "assistant", content: msg.content });
      var message = msg.content.replaceAll("\n", "<br>");
      if (
        Math.floor(chatmsg_div.scrollTop + chatmsg_div.clientHeight) + 50 >
        chatmsg_div.scrollHeight
      ) {
        setTimeout(scrolldownchat, 500);
      }
      hideChatLoading();
      $("#chat-body").append(
        '<div class="chat-msg-box"><div class="chat-icon"><img src="' +
          bot_img +
          '" alt="chat-icon" /></div><div class="chat-content"><p class="role">Chatbot</p><div class="chat-msg">' +
          message +
          '</div></div></div>'
      );
    });
  });

  $("#start-form").on("submit", (e)=>{
    e.preventDefault();

    temp = parseFloat($("#creative-val").val());
    $(".intro").addClass("d-none");
    $(".chat-component").removeClass("d-none");
    setTimeout(() => {
      $(".chat-loading").addClass("loading");
    }, 300);
    console.log(temp);
  });
});
