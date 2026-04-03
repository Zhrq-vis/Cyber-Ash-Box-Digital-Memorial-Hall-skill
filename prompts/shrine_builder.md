# Digital Shrine Builder

你的任务是把新生成的纪念体写入 **电子纪念堂 / Digital Shrine** 索引。

每个条目包括：
- name
- slug
- relationship
- birth_year
- death_year
- one_line_epitaph
- created_at

输出示例：

```json
{
  "hall_name": "数字祠堂",
  "entries": [
    {
      "name": "张三",
      "slug": "zhangsan",
      "relationship": "父亲",
      "birth_year": "1958",
      "death_year": "2024",
      "one_line_epitaph": "他沉默寡言，却把一生都活成了责任。",
      "created_at": "2026-04-03T09:00:00"
    }
  ]
}
```
