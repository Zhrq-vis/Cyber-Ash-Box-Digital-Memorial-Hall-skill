# 增量合并逻辑（Memorial / Persona / Epitaph / Timeline）

当用户追加新材料时，把增量信息 merge 到现有纪念档案中。

## 可更新的文件
- `memorial.md`
- `persona.md`
- `epitaph.md`
- `timeline.md`
- `shrine.json`

## 合并原则

### Memorial Memory（事实类）
适合放入：
- 新的生平事件
- 新的家庭关系信息
- 新的习惯与价值观证据
- 新的“别人怎么记得 TA”的片段

### Voice Persona（表达类）
适合放入：
- 新的口头禅
- 新的语气证据
- 新的情绪表达方式
- 明显不像 TA 会说的话

### Epitaph / Eulogy / Timeline
如新增材料改变整体理解，可重写：
- 墓志铭
- 悼词
- 时间线

## 严格要求
- 增量追加优先，不轻易覆盖原有高置信结论
- 新证据与旧结论冲突时，要标明冲突点
- 不要因为新增一段文字就把整个人写偏
