// {
//     // 設定
//     const tocInsertElement = document.querySelector('#toc');
//     const headingElements = document.querySelectorAll('.post-detail h2, .post-detail h3, .post-detail h4, .post-detail h5, .post-detail h6');
//     const toc = document.createElement('ol');
//     let id = 0;

//     headingElements.forEach(el => {
//         const rank = Number(el.tagName.substring(1)) - 2; // h2 から始まるので、2を引く
//         let currentToc = toc;

//         // 適切な階層まで下がる
//         for (let i = 0; i < rank; i++) {
//             if (!currentToc.lastElementChild) {
//                 currentToc.appendChild(document.createElement('li'));
//             }
//             if (!currentToc.lastElementChild.lastElementChild) {
//                 currentToc.lastElementChild.appendChild(document.createElement('ol'));
//             }
//             currentToc = currentToc.lastElementChild.lastElementChild;
//         }

//         // リンクを作成して追加
//         const li = document.createElement('li');
//         const a = document.createElement('a');
//         el.id = el.id || `heading${id++}`;
//         a.href = `#${el.id}`;
//         a.textContent = el.textContent;
//         a.className = 'tocLink';
//         li.appendChild(a);
//         currentToc.appendChild(li);
//     });

//     // 目次を挿入
//     if (tocInsertElement && toc.childElementCount > 0) {
//         tocInsertElement.appendChild(toc);
//     }
// }


document.addEventListener("DOMContentLoaded", function () {
    tocbot.init({
        tocSelector: "#toc",
        contentSelector: ".post-detail",
        headingSelector: "h2, h3",
        headingsOffset: 1,
        collapseDepth: 3, // 表示する見出しの深さを調整
        scrollSmooth: false,
        hasInnerContainers: true,
    });
    
});