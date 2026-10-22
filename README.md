# Villager Golem Mod (Forge 1.20.1)

## ساخت جار با GitHub Actions (بدون نصب چیزی)
1. توی GitHub یه ریپوی جدید بساز (Public یا Private).
2. همه‌ی محتویات این پوشه رو آپلود کن (Add file > Upload files). حتماً پوشه‌ی `.github` هم باید آپلود بشه.
3. برو تب **Actions**؛ بیلد خودکار شروع می‌شه (حدود ۵ تا ۱۰ دقیقه).
4. وقتی تموم شد، روی اجرا کلیک کن و پایین صفحه از بخش **Artifacts** فایل `villagergolem-jar` رو دانلود کن.
5. زیپ رو باز کن و جار رو بنداز توی پوشه `mods` ماینکرفت.

## ویژگی‌ها
- Villager Golem: HP 120، سریع‌تر و قوی‌تر از آیرون گولم
- با شمش طلا درمان می‌شه
- Spawn Egg + دستور `/summon villagergolem:villager_golem`

## ساخت روی سیستم خودت
JDK 17 + Gradle 8.1.1 نصب کن و بزن `gradle build`
