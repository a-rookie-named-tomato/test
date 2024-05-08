// $(document).ready(function () {
//     const websocket = new WebSocket("ws://127.0.0.1:12345/client/ws");
//     let shouldContinue = true;

//     websocket.onmessage = function (event) {
//         if (!shouldContinue) {
//             return;
//         }

//         const rawData = event.data;
//         console.log("Raw Data:", rawData);

//         try {
//             const data = JSON.parse(rawData);
//             console.log("Parsed Data:", data);
//             displayData(data);
//         } catch (error) {
//             console.error("Error parsing data:", error);
//         }
//     };

//     function displayData(data) {
//         const dataList = $("#dataList");
//         dataList.empty();

//         // 手动添加指定的字段
//         const fieldMappings = [
//             "车辆编号", "车型", "制造商", "颜色", "年份", "在售价格(万)", "购买者", "电话", "店铺id", "售出时间", "售出时间","在售状态"
//         ];

//         data.forEach(function (record) {
//             const listItem = document.createElement("li");
//             listItem.classList.add("list-group-item");

//             fieldMappings.forEach(function (fieldName, index) {
//                 const fieldValue = record[index] || "N/A";
//                 listItem.innerHTML += `<strong>${fieldName}:</strong> ${fieldValue}<br>`;
//             });

//             dataList.append(listItem);
//         });
//     }

//     window.addEventListener("beforeunload", function () {
//         shouldContinue = false;
//         websocket.close();
//     });
// });


$(document).ready(function () {
    const websocket = new WebSocket("ws://127.0.0.1:12345/client/ws");
    let shouldContinue = true;

    websocket.onmessage = function (event) {
        if (!shouldContinue) {
            return;
        }

        const rawData = event.data;
        console.log("Raw Data:", rawData);

        try {
            const data = JSON.parse(rawData);
            console.log("Parsed Data:", data);
            displayData(data);
        } catch (error) {
            console.error("Error parsing data:", error);
        }
    };

    function displayData(data) {
        const table = $("#dataTable");
        table.empty();
    
        // 手动添加指定的字段
        const fieldMappings = [
            "车辆编号", "车型", "制造商", "颜色", "年份", "在售价格(万)", "购买者", "电话", "店铺id", "售出时间", "售出时间", "在售状态"
        ];
    
        // 创建表头
        const thead = document.createElement("thead");
        const headerRow = document.createElement("tr");
    
        fieldMappings.forEach(function (fieldName) {
            const th = document.createElement("th");
            th.textContent = fieldName;
            headerRow.appendChild(th);
        });
    
        thead.appendChild(headerRow);
        table.append(thead);
    
        // 创建表格内容
        const tbody = document.createElement("tbody");
    
        data.forEach(function (record) {
            const row = document.createElement("tr");
    
            fieldMappings.forEach(function (fieldName, index) {
                const fieldValue = record[index] || "N/A";
                const cell = document.createElement("td");
                cell.innerHTML = fieldValue;
                row.appendChild(cell);
            });
    
            tbody.appendChild(row);
        });
    
        table.append(tbody);
    }
    

    window.addEventListener("beforeunload", function () {
        shouldContinue = false;
        websocket.close();
    });
});


