function searchPage() {
    var searchText = $('#searchInput').val(); // 検索ボックスからテキストを取得

    // テキストが入力されていない場合の処理
    if (!searchText.trim()) {
        // 検索窓にメッセージを表示
        $('#searchInput').attr('placeholder', 'ここに文字を入力');
        return; // これ以上の処理を行わない
    }

    var regex = new RegExp('(' + searchText + ')', 'gi'); // 大文字小文字を区別しない正規表現

    // 既存のハイライトをクリアする
    $('.post-block').find('.highlight').each(function() {
        $(this).replaceWith($(this).text());
    });

    var found = false;
    var firstHighlighted = null; // 最初のハイライトされた要素を格納する変数

    $('.post-block').each(function() {
        var block = $(this);
        var blockHtml = block.html();

        // テキストが含まれる場合，ハイライトを適用
        if (block.text().toLowerCase().indexOf(searchText.toLowerCase()) !== -1) {
            blockHtml = blockHtml.replace(regex, "<span class='highlight'>$1</span>");
            block.html(blockHtml);

            if (!found) {
                firstHighlighted = block; // 最初のハイライトされた要素を保存
                found = true;
            }
        }
    });

    // ハイライトされた要素があれば，その要素にスクロール
    if (firstHighlighted) {
        $('html, body').animate({
            scrollTop: firstHighlighted.offset().top
        }, 300);
    } else {
        // ハイライトされた要素がない場合，メッセージを表示
        $('#noResults').show();
    }
}


// function SuccessPOP() {
//     document.getElementById("submit-button").addEventListener("click", function() {
//         var nameField = document.getElementById("id_name").value;
//         var emailField = document.getElementById("id_email").value;
//         var messageField = document.getElementById("id_message").value;

//         if (nameField.trim() === "") {
//             alert("名前を入力してください。");
//         } 
//         else if (emailField.trim() === "") {
//             alert("メールアドレスを入力してください。");
//         } 
//         else if (messageField.trim() === "") {
//             alert("メッセージを入力してください。");
//         }
//         else {
//             alert("メッセージを送信しました！");
//         }
//     });
// }


function SuccessPOP() {
    document.getElementById("submit-button").addEventListener("click", function() {
        var nameField = document.getElementById("id_name").value;
        var emailField = document.getElementById("id_email").value;
        var messageField = document.getElementById("id_message").value;

        if (nameField.trim() === "") {
            alert("名前を入力してください。");
            return; // 名前が空の場合、ここで処理を停止
        } 
        if (emailField.trim() === "") {
            alert("メールアドレスを入力してください。");
            return; // メールアドレスが空の場合、ここで処理を停止
        } 
        if (messageField.trim() === "") {
            alert("メッセージを入力してください。");
            return; // メッセージが空の場合、ここで処理を停止
        }

        alert("メッセージを送信しました！");
    });
}



// ボタンのクリックイベントを設定
$('button').on('click', function() {
    searchPage();
    SuccessPOP();
});





