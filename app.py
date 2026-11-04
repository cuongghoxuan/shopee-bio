import json

# Thay ID tài khoản Affiliate của bạn vào đây
YOUR_AFFILIATE_ID = "17344610097" 

def convert_to_affiliate_link(original_url, sub_id="bio_page"):
    if "?" in original_url:
        return f"{original_url}&utm_source=an_123456789&utm_medium=affiliate&aff_id={YOUR_AFFILIATE_ID}&sub_id={sub_id}"
    else:
        return f"{original_url}?utm_source=an_123456789&utm_medium=affiliate&aff_id={YOUR_AFFILIATE_ID}&sub_id={sub_id}"

def fetch_latest_vouchers():
    # Dữ liệu mẫu voucher
    raw_deals = [
        {
            "id": 1,
            "title": "Mã Freeship Extra 0Đ",
            "code": "FREESHIP0D",
            "discount": "Giảm 100% phí ship",
            "url": "https://shopee.vn/m/mien-phi-van-chuyen",
            "category": "voucher",
        },
        {
            "id": 2,
            "title": "Voucher Điện Tử Giảm 50K",
            "code": "TECH50K",
            "discount": "Giảm 50K đơn 250K",
            "url": "https://shopee.vn/m/ma-giam-gia",
            "category": "voucher",
        },
    ]

    processed_deals = []
    for deal in raw_deals:
        deal["aff_link"] = convert_to_affiliate_link(deal["url"])
        processed_deals.append(deal)

    return processed_deals

if __name__ == "__main__":
    deals = fetch_latest_vouchers()
    with open("deals.json", "w", encoding="utf-8") as f:
        json.dump(deals, f, ensure_ascii=False, indent=4)
    print("Đã cập nhật deals.json thành công!")