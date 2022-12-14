/*jshint esversion: 6 */

function like(postId) {
  const likeCount = document.getElementById(`likes-count-${postId}`);
  const likeButton = document.getElementById(`like-button-${postId}`);

  fetch(`/like-post/${postId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data.likes;
      if (data.liked === true) {
        likeButton.className = "fas fa-thumbs-up fa-xl";
      } else {
        likeButton.className = "far fa-thumbs-up fa-xl";
      }
    })
    .catch((e) => alert("There was an error liking this post."));
}