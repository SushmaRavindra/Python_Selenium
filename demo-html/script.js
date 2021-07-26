const display = function () {
    fname = document.querySelector("#firstname").value
    lname = document.querySelector("#lastname").value
    alert(`Hello ${fname}, ${lname}`)
    document.querySelector("#firstname").value = ""
    document.querySelector("#lastname").value = ""
}
document.querySelector("#submit").addEventListener("click", display)

document.querySelector("#delete").addEventListener("click", function () {
    if (window.confirm("Are You Sure You Want to Delete")) {
        document.querySelector(".label_alert").textContent = "You clicked Ok!!!"
    } else {
        document.querySelector(".label_alert").textContent = "You clicked Cancel !!!"
    }
})

document.querySelector("#iphone").addEventListener("click", function () {
    document.querySelector("#buy").textContent = "iPhone Added to Cart"
})

const dbl = function () {
    document.querySelector("#double-click-message").textContent = "You double clicked"
}

