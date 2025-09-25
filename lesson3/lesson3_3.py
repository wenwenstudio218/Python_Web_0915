import tools

def main():
    try:
        data = tools.download_youbike_data()
        areas = tools.get_area(data)
        # print(areas)
        print("目前可以查詢的區域：\n")
        for area in areas:
            print(area,end=" ")
        print("\n")
        selected = input("請選擇一個區域：")
        if selected not in areas:
            print("查無此區域，請重新執行程式")
            return
        sites_of_area = tools.get_sites_of_area(data, selected)
        print(f"\n{selected} 區的站點資訊：")
        for site in sites_of_area:
            # 只顯示站點名稱與可借車輛數
            print(f"站點：{site['sna']}，可借車輛：{site['sbi']}")

    except Exception as e:
        print(f"發生錯誤\n{e}")

if __name__ == "__main__":
    main()
