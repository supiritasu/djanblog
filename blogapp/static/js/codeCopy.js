function copyCode(btn) {
    var originalText = btn.textContent; // 元のテキストを保存
    btn.textContent = 'Copied!'; // ボタンのテキストを変更

    // 2秒後に元のテキストに戻す
    setTimeout(function() {
        btn.textContent = originalText;
    }, 2000);

    var codeElement = btn.nextElementSibling.nextElementSibling; // コード要素を取得

    if (codeElement && codeElement.textContent) {
        var code = codeElement.textContent;

        // Clipboard APIを使用してコピー
        navigator.clipboard.writeText(code).then(function() {
        }).catch(function(error) {
            console.error('コピーに失敗しました:', error);
        });
    } else {
        console.error('コピーするコードが見つかりませんでした。');
    }
}
