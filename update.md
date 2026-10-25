# 统一更新日志

## 汇总说明

- 汇总日期：2026-10-25
- 状态截止：2026-10-25
- 来源文件：
  - `/home/maptex/Code/xcsmartdatabase/clis` 下各子仓库 Git log
  - `/home/maptex/Code/xcsmartdatabase/gisagent` Git log
  - `/home/maptex/Code/xcsmartdatabase/skills` 下各技能独立仓库 Git log（以 `known-skills.manifest` 为 subgroup 清单）
- 说明：
  - 本文件由 `doc/scripts/generate_skill_update.py` 自动生成。
  - 汇总范围固定为 `clis/`、`gisagent/` 与 `skills/`。
  - 这不是逐个 `SKILL.md` 自动生成的全量 changelog，而是对固定来源 Git 提交的统一汇总。
  - `skills/` 的 subgroup 口径与同步结论以 `config/openspecs/changes/docker-sync-skills/README.md` 索引的 `openspec/changes/sync-skills-from-gitlab/` 记录为准。

## 更新概览

- **`clis/` 持续演进**：`9` 个子仓库新增 `125` 条提交，重点集中在 `postgis_service_cli、knowledge_cli、postgiscli`。
- **`gisagent/` 继续迭代**：累计 `110` 条提交，最近更新到 `2026-10-23`。
- **`skills/` 逐技能仓库持续演进**：`44` 个技能仓库新增 `184` 条提交，最近更新到 `2026-10-25`。

---

## clis/

### 本轮状态

- 来源：`/home/maptex/Code/xcsmartdatabase/clis` 下各子仓库 Git log
- 统计区间：2026-06-10 至 2026-10-25
- 本轮共有 `9` 个子仓库发生更新，累计 `125` 条提交
- 最近更新日期：`2026-09-29`
- 重点仓库：`postgis_service_cli、knowledge_cli、postgiscli`

### `3dtiles_cli`

- 提交数：`16`，区间：`2026-06-24` 至 `2026-09-29`
- `2026-06-24` `419d211` Initial 3dtiles_cli implementation
- `2026-06-25` `8668da7` feat: improve vector texture export defaults
- `2026-06-25` `aac3aa3` feat:add docker env
- `2026-06-25` `3b634c2` feat:add gitignore
- `2026-06-26` `7373887` feat: use ogr2ogr for shapefile vectors
- `2026-06-26` `14ad61d` env: update docker env
- `2026-07-03` `92b46e9` feat: add OBJ split tiling and geology mesh support
- `2026-07-06` `9904a78` ci: add open code review pipeline
- `2026-07-06` `70aedb8` ci: retry alpine package install
- `2026-07-08` `a480ea9` feat: add docker env
- `2026-07-16` `12ff913` fix: preserve OBJ UV coordinates without textures
- `2026-09-20` `726a5a2` feat: add arnis voxel-city 3D Tiles export
- `2026-09-20` `63b6d36` feat:add docker package
- `2026-09-24` `2e46d69` feat: use arnis voxel LOD meshes instead of box proxies
- `2026-09-25` `22c6d4a` feat: pack multi-LOD arnis leaves and share per-layer atlas
- `2026-09-29` `f78208a` feat: default arnis tiles to coarse LOD packing and Draco compression

### `arnis_cli`

- 提交数：`9`，区间：`2026-09-20` 至 `2026-09-29`
- `2026-09-20` `6af9f7a` feat: add arnis-cli voxel city skill and generator
- `2026-09-20` `b692fbd` fix: keep a single Three.js preview page
- `2026-09-20` `b983127` fix: center arnis bbox on tianditu geocode
- `2026-09-20` `8646e9e` build: refresh Windows and Linux musl skill binaries
- `2026-09-22` `5a1bab4` feat:add docker deps
- `2026-09-22` `e6578e4` feat:add change bin
- `2026-09-24` `040d612` feat: emit range-based voxel LOD meshes for 3D Tiles
- `2026-09-24` `f42e57c` fix: generate OSM layer=-1 podium and sunken buildings
- `2026-09-29` `f8e9608` fix: keep thin roads at coarse voxel LOD and raise building Y ceiling

### `geoscan_desktop`

- 提交数：`10`，区间：`2026-08-07` 至 `2026-09-28`
- `2026-08-07` `b7a30a5` Initial import of GeoScan Desktop 0.7
- `2026-08-11` `6619f1a` fix: align agent workflow and desktop processing
- `2026-08-12` `d9be7d9` fix: harden desktop agent recognition pipeline
- `2026-09-09` `50ef881` feat: improve desktop map editing and processing workflow
- `2026-09-26` `aaa49e1` doc: add openspec & pdf
- `2026-09-27` `5ab9ce1` feat:add user pdf
- `2026-09-27` `9668200` build: package licence assets and cover them with unit tests
- `2026-09-27` `d82ddd1` docs: brand the manual pages with MapGIS
- `2026-09-27` `0124e81` build: stop tracking the rendered manual PDF
- `2026-09-28` `aa331f4` doc: add user manuer html

### `mapgis67_cli`

- 提交数：`8`，区间：`2026-07-29` 至 `2026-09-28`
- `2026-07-29` `63821d0` Add MapGIS67 CLI writers and tests
- `2026-07-29` `5fe3d22` Add specifications, skills, and support scripts
- `2026-07-30` `128320f` feat:add ui control  mapgis67
- `2026-08-11` `654db19` Add WAT to WT conversion workflow
- `2026-09-21` `818fe7a` Record the palette colorNo mapping route so it is reproducible
- `2026-09-21` `54ee26a` Recreate stale GVFS mount symlink
- `2026-09-28` `3cbf41d` feat:add origin data
- `2026-09-28` `2230748` feat:updatae skill

### `geoscan_cli`

- 提交数：`6`，区间：`2026-08-07` 至 `2026-09-26`
- `2026-08-07` `da7a461` Initial import of GeoScan CLI 2.1.1
- `2026-08-11` `7a6cf1c` feat: align agent workflow and decouple skill rendering
- `2026-08-12` `344f094` feat: improve staged legend recognition workflow
- `2026-09-09` `5736b91` feat: optimize geologic map workflow and diagnostics
- `2026-08-11` `dbf287e` fix frozen tiled worker process pool startup
- `2026-09-26` `1dfbd6a` feat:add doc and pdf for user

### `postgiscli`

- 提交数：`18`，区间：`2026-06-29` 至 `2026-09-02`
- `2026-06-29` `d4fd258` feat: update Dockerfile and skill documentation
- `2026-07-06` `818e32e` ci: add open code review pipeline
- `2026-07-06` `9da7961` ci: retry alpine package install
- `2026-07-08` `7449ae5` feat:add docker env
- `2026-07-20` `14e33a3` chore: sync local changes 2026-07-20
- `2026-09-02` `02d04df` ci: add validate and docker build stages for postgiscli
- `2026-09-02` `6e29492` ci: use domestic registry mirrors for job images
- `2026-09-02` `1cda9b4` ci: runner pull_policy if-not-present to avoid registry hang
- `2026-09-02` `95d5e3d` ci: switch to domestic apt/pip/npm mirrors for build isolation
- `2026-09-02` `69e1159` ci: retest with domestic mirrors
- `2026-09-02` `5d2513a` ci: probe validate output
- `2026-09-02` `0e2d04d` ci: add --break-system-packages for PEP668 on alpine pip
- `2026-09-02` `8940aec` ci: observation run
- `2026-09-02` `18a57f0` ci: enable ocr review with api key
- `2026-09-02` `32c59a8` ci: install bash in docker build job via domestic apk
- `2026-09-02` `f3a193c` ci: drop docker:build, use compose.ci build recipe for monorepo
- `2026-09-02` `c4719de` ci: re-run pipeline test
- `2026-09-02` `292fd00` ci: demo full pipeline flow

### `knowledge_cli`

- 提交数：`18`，区间：`2026-06-11` 至 `2026-08-17`
- `2026-06-11` `4096016` feat: refine knowledge graph g6 rendering
- `2026-06-14` `6e6c364` chore: sync workspace changes
- `2026-06-14` `1fa1675` chore: sync workspace changes
- `2026-06-23` `7b8c522` Refine knowledge skill trigger rules
- `2026-06-29` `94aa42b` feat: update knowledge-mcp and graph-g6-render
- `2026-07-06` `1f0b91f` ci: add open code review pipeline
- `2026-07-06` `707d57d` ci: retry alpine package install
- `2026-07-08` `3676308` feat:add nautical knowlidge
- `2026-07-20` `779bd86` chore: sync local changes 2026-07-20
- `2026-08-04` `d5922ab` Add GitLab CI pages and knowledge graph jobs
- `2026-08-04` `302b03a` Harden nautical CI validation job
- `2026-08-17` `87f85cb` feat:update skill
- `2026-08-17` `f2d455f` feat:add scripts
- `2026-08-17` `b6da36c` feat:add openspec
- `2026-08-17` `f949453` feat: add agent runtime sources and nautical scripts
- `2026-08-17` `50d24ee` feat:add doc
- `2026-08-17` `bb410e4` chore: ignore generated knowledge outputs
- `2026-08-17` `f5d69a0` feat: add nautical SVG review UI

### `postgis_service_cli`

- 提交数：`34`，区间：`2026-06-10` 至 `2026-07-20`
- `2026-06-10` `61b5899` env:fix docker var
- `2026-06-11` `f235ec9` Refine MapLibre gateway style guidance
- `2026-06-11` `5b774a4` docs: update postgis service skill sprite path
- `2026-06-16` `c55012f` Add 3D Tiles publishing and Cesium preview support
- `2026-06-16` `6ecc556` docs: clarify 3dtiles source boundary
- `2026-06-16` `0b1af57` docs: record 3dtiles publishing smoke test
- `2026-06-16` `2279b67` fix: reject 3dtiles manifest symlink escapes
- `2026-06-16` `8693470` docs: archive 3dtiles openspec changes
- `2026-06-16` `e83c5b5` ci: use precompiled maplibre native by default
- `2026-06-16` `bb8b303` test: align server tests with gateway state
- `2026-06-16` `11b572e` test: restore pg server fixture initialization
- `2026-06-16` `f05e53b` test: align pg table sources with qualified ids
- `2026-06-17` `58700ea` Add repeatable mainland 3dtiles ingest pipeline
- `2026-06-25` `4ef0421` feat: expand 3dtiles support and discovery
- `2026-06-26` `e6ce584` docs: sync postgis service skill with 3dtiles guidance
- `2026-06-26` `b2034ea` Merge branch 'main' into 3dtile
- `2026-06-28` `fcc3c68` Add OSM building materials catalog
- `2026-06-28` `bb15b85` Add material catalog URLs
- `2026-06-29` `a354325` feat: update materials-catalog and postgres-3dtiles-source
- `2026-07-08` `209b46b` Add hk260702 pipe 3dtiles prepare script
- `2026-07-08` `4f491b4` Align hk260702 valve center offset from model geometry
- `2026-07-08` `edd7d64` Revert invalid hk260702 valve offset formula
- `2026-07-08` `d401145` Use PostGIS oracle normals for hk260702 valves
- `2026-07-08` `49b8e62` Persist hk260702 pipe transparency
- `2026-07-08` `a5d9da7` Restore hk260702 valve asset node transforms
- `2026-07-08` `4bbb056` Use baked hk260702 valve instancing asset
- `2026-07-08` `39a2212` Orient hk260702 valves along pipe tangents
- `2026-07-08` `37f4bfb` Fix hk260702 valve local up orientation
- `2026-07-08` `38d5f25` Restore hk260702 pipe opacity and halve radius
- `2026-07-08` `6665216` Make hk260702 pipe material visible
- `2026-07-08` `d63c23a` Lift hk260702 pipe body above terrain
- `2026-07-08` `0c7e817` Strip invalid hk260702 pipe GLB metadata
- `2026-07-08` `b6ec828` Expand 3dtiles auto-discovery and catalog tooling
- `2026-07-20` `b7225d8` chore: sync local changes 2026-07-20

### `geomoder_cli`

- 提交数：`6`，区间：`2026-07-03` 至 `2026-07-17`
- `2026-07-03` `0ed380a` Initial geomoder_cli import
- `2026-07-06` `ac74a68` ci: add open code review pipeline
- `2026-07-06` `27d4f0f` ci: retry alpine package install
- `2026-07-08` `d54ae27` feat: add docker env
- `2026-07-16` `1341aca` feat: improve geological volume modeling pipeline
- `2026-07-17` `7559bce` Fix optional Docker dependencies


## gisagent/

### 本轮状态

- 来源：`/home/maptex/Code/xcsmartdatabase/gisagent` Git log
- 统计区间：2026-06-10 至 2026-10-25
- 本轮累计 `110` 条提交
- 最近更新日期：`2026-10-23`

### 提交列表

- `2026-06-10` `5725df5` fix: flatten grouped skills in docker user runtimes
- `2026-06-10` `78b6aa5` merge: phase2 user runtime sandbox
- `2026-06-10` `596a4e7` fix:uplaod large file
- `2026-06-10` `0f374fc` 优化对话容易卡死问题
- `2026-06-10` `c67d890` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/gisagent
- `2026-06-10` `36a9f82` 分享社区时可以选择技能
- `2026-06-10` `ab86583` fix: error url make error
- `2026-06-10` `e3074db` fix: harden web server and sse runtime stability
- `2026-06-11` `a578463` 收藏改成点赞
- `2026-06-11` `d9857bb` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/gisagent
- `2026-06-11` `1ac9c50` 优化对话和修改解绑逻辑
- `2026-06-14` `ebb9491` feat(gis): configure enterprise wechat community qr
- `2026-06-14` `9fdaf7f` feat:add e2e test for http and https
- `2026-06-15` `b3c2843` 优化对话，添加帮助链接
- `2026-06-15` `2bad330` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/gisagent
- `2026-06-15` `98022c1` 合并代码
- `2026-06-16` `d270dcd` 优化做同款
- `2026-06-16` `b7c38ef` feat:add e2e test
- `2026-06-16` `20b55aa` 更新社区浏览计数
- `2026-06-16` `da37f63` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/gisagent
- `2026-06-17` `1d1b3f3` fix: correct help docs link
- `2026-06-17` `d7ed165` 优化对话的效率和状态管理
- `2026-06-17` `e31ff81` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/gisagent
- `2026-06-18` `a4e71e4` 输入框自适应
- `2026-06-18` `2e183db` fix: redirect webui routes to services path
- `2026-06-23` `b03beb7` Update community QR image
- `2026-06-25` `a092857` chore: sync workspace changes
- `2026-06-28` `f8c518f` feat: add user analysis dashboard exports
- `2026-06-28` `4d59e98` test: add qwen30b regression tooling
- `2026-06-29` `8f0344f` feat: add qwen30b distillation scripts and update tests
- `2026-07-03` `94cadec` Fix auth metadata and tool call display
- `2026-07-03` `6043652` feat:add openspec and test for small llm
- `2026-07-03` `b599eab` fix: restore code to mergetool
- `2026-07-04` `d86e067` feat: 更新用户分析功能
- `2026-07-06` `3abaf5a` Revert "feat: 更新用户分析功能"
- `2026-07-06` `d859863` Add GIS attachments and daily web logs
- `2026-07-06` `7999689` Revert "feat: add user analysis dashboard exports"
- `2026-07-07` `ea1b9ad` feat: add forced password reset flow
- `2026-07-17` `a2d95fe` feat: add session file archive download
- `2026-07-22` `04a339e` feat: add GIS Agent license enforcement and console
- `2026-07-22` `8b0a354` chore: restore agent config
- `2026-07-22` `607eb3d` chore: add license console signing keys
- `2026-07-22` `3f95549` feat:update wechat
- `2026-08-09` `6c73776` feat: update docker license packaging and wechat assets
- `2026-08-17` `5b48149` feat: improve registration and session rename UX
- `2026-08-17` `8de259b` fix: restrict session file downloads
- `2026-08-17` `f1eee5c` feat:add doc for code use right
- `2026-08-21` `2a34a27` feat: allow editing invite code usage limits
- `2026-08-24` `506aa19` fix: localize auth error messages
- `2026-08-25` `fa1627c` feat: remember user session mode and model
- `2026-08-25` `e658546` fix: refresh unavailable preferred model
- `2026-08-25` `cdda881` feat:add docker config replace
- `2026-08-26` `97f5454` fix: update preferences from archived sessions
- `2026-08-26` `a77d274` Expose provider catalog for Claude agent models
- `2026-08-27` `9cba15b` Fix qwen prompt bootstrap for bind mounts
- `2026-08-27` `5746ed3` Clean up failed docker agent startups
- `2026-08-27` `384780d` Clear agent binding after failed session startup
- `2026-08-27` `9ab4c22` Stop runtime after failed web session create
- `2026-08-27` `2db5575` feat:update wechat picture
- `2026-08-27` `3ffb45e` chore: bilingualize user-facing errors
- `2026-08-28` `9afe810` fix: set utf8 charset for error responses
- `2026-08-30` `87fe539` feat: remove  wechat text
- `2026-08-31` `a13f429` feat: pass whitelisted env vars to ACP agents
- `2026-08-31` `2bdafe6` chore: add postgis service cli dir to startup path
- `2026-08-31` `54e17a4` docs: clarify postgis service cli env passthrough
- `2026-09-01` `90dc65e` feat: add admin session HTML preview
- `2026-09-01` `3fd11cb` feat: soft delete sessions with admin purge
- `2026-09-01` `096115c` feat:add dynamic rotate key
- `2026-09-02` `d80f05b` chore: unify concurrent session limit
- `2026-09-03` `777ffc7` feat:add secrets key for agent acp
- `2026-09-09` `38fd1f3` Revert "feat:add secrets key for agent acp"
- `2026-09-09` `9b9ccb9` feat: pass env-backed provider keys to ACP agents
- `2026-09-11` `99aae7e` feat:change gisagent env for precess param
- `2026-09-13` `23f869f` gisagent: finalize agent runtime configuration
- `2026-09-14` `dea4366` merge: sync latest main while preserving local agent config
- `2026-09-14` `d8bf84b` feat:change docker env
- `2026-09-14` `9193617` refactor: remove hardcoded runtime behavior
- `2026-09-14` `61764c0` merge: sync GitLab updates while preserving local runtime logic
- `2026-09-14` `7f841d5` fix: localize file limit messages
- `2026-09-17` `fae1daa` feat:change homepage style
- `2026-09-17` `e9aebeb` feat:add custom skill & mcp code
- `2026-09-17` `14b0d26` revert: restore agent-manager runtime env handling
- `2026-09-20` `6cf221e` feat: extract customizable GIS homepage overlay
- `2026-09-20` `1426f96` feat: raise community publish asset size limits
- `2026-09-22` `9f01df0` feat: add product /lib map engines and admin list paging
- `2026-09-22` `e0c99e9` feat: switch product Cesium engine to 1.122
- `2026-09-22` `4cd0731` env:add wechat readme for qr
- `2026-09-29` `f9746de` feat: add themed GIS homepage showcase cases
- `2026-09-29` `f20b40f` feat: rename homepage hero title to MapGIS Agent时空智能体
- `2026-09-29` `30bc456` feat: add terms and privacy links on login and register
- `2026-09-30` `02315bc` feat: enrich homepage showcase remix prompts
- `2026-09-29` `78b3619` feat:update wechat jpg
- `2026-10-08` `b058c9b` feat:update docker env
- `2026-10-10` `b0fc1df` feat: add website WeChat login and conversation navigation
- `2026-10-10` `ab52ad6` fix: resume WeChat login after top-level callback
- `2026-10-10` `d4b98e1` fix: move WeChat binding form into login column
- `2026-10-10` `57c6414` feat: add WeChat profile and account settings
- `2026-10-12` `8cc0783` fix: polish GIS UI and persist WeChat avatars
- `2026-10-12` `5e09317` feat:update wechat qr
- `2026-10-21` `55a555d` feat: package Atlas Earth and support ranged static assets
- `2026-10-21` `b1c8be9` Merge remote-tracking branch 'origin/main'
- `2026-10-21` `f735733` feat:update qr
- `2026-10-22` `ca87450` fix: range-serve admin previews and add account binding
- `2026-10-22` `6a8ed26` feat: add map style details to fabric and poster prompts
- `2026-10-22` `092c487` feat: update Atlas runtime bundle and context workers
- `2026-10-22` `a3e0b87` fix: reuse registered SMS copy for phone bind
- `2026-10-23` `da34d3b` feat: refresh Atlas bundle and context worker hashes
- `2026-10-23` `8223b6b` chore: drop unused Atlas overture worker hashes
- `2026-10-23` `394169a` feat: update Atlas mesh worker hash
- `2026-10-23` `3918709` feat: refresh Atlas runtime bundle


## skills/

### 本轮状态

- 来源：`/home/maptex/Code/xcsmartdatabase/skills` 下各技能独立仓库 Git log（GitLab `xcsmartdatabase/skills` subgroup 清单：`known-skills.manifest`）
- 统计区间：2026-06-10 至 2026-10-25
- 本轮共有 `44` 个技能仓库发生更新，累计 `184` 条提交
- subgroup 清单共 `51` 个技能，其余 `7` 个在区间内无提交
- 最近更新日期：`2026-10-25`
- 重点仓库：`tianditu-1m-atlas、cesium-common、3d-building-map`
- 不在 subgroup 清单内的本地缓存目录（不计入统计，不参与 `skillpacks/mapviz-skills/` 提升）：`agent-orchestration-improve-agent`、`evolution`、`postgis-3dtiles`、`ui-ux-pro-max-skill`

### `tianditu-1m-atlas`

- 提交数：`41`，区间：`2026-10-18` 至 `2026-10-25`
- `2026-10-18` `c4b928e` feat:init version
- `2026-10-19` `7c324c6` feat:hydro charts bind to province stats ledger
- `2026-10-19` `9364c17` feat: align hydro charts between skill and product template
- `2026-10-19` `1a3aa41` feat: align hydro charts between skill and product template
- `2026-10-19` `e5be16d` feat: add province mask selector and zoom
- `2026-10-19` `b6e02ae` fix: sync geology module and chart controls
- `2026-10-21` `90a5665` fix: pack hydro brief and size table cards by row count
- `2026-10-21` `b011b15` feat: add geology overlay as sixth mode in product template
- `2026-10-21` `3ed1630` feat: atlas layout for geology statistics cards
- `2026-10-21` `7f1b655` style: paper sheet chrome for the product template
- `2026-10-21` `945ce0a` style: sheet chrome follows the active mode
- `2026-10-21` `07ff105` fix: guard map remount against double remove on rapid mode switching
- `2026-10-21` `c31fb92` perf: limit vector tile requests to the masked province
- `2026-10-22` `a919f25` feat: geologic time table and fault cross-section for geology mode
- `2026-10-22` `833d719` feat: stratigraphic column and sheet index for geology mode
- `2026-10-22` `337bb56` docs: consolidate SKILL.md for the template atlas round
- `2026-10-22` `a907c0a` feat: digital/print layout switch for geology mode
- `2026-10-22` `9a95753` feat: atlas column layout for qianhu/dajiang hydro themes
- `2026-10-22` `853ef30` style: hydro chart colors from each theme's map palette
- `2026-10-22` `7dc7d26` feat: linked ledger between hydro tables and map
- `2026-10-22` `f1b82d2` fix: move hydro entrance/relink lines out of renderGgwTable
- `2026-10-22` `918d58a` feat: digital/print layout switch for std, print per GB/T 20257.1 fig C.1
- `2026-10-22` `6e0a831` fix: single C.1 frame in std print layout
- `2026-10-22` `89aabb8` fix: sheet number under title in std print; white paper for std
- `2026-10-22` `bd854ce` feat: std digital map furniture; fix its leak; geology print scale under legend
- `2026-10-22` `5f23c47` feat: map furniture for v3 and ngcc digital layouts
- `2026-10-22` `e33102c` style: one card style for layers, legend, sheet index and scale
- `2026-10-22` `2796101` fix: in-map cards follow the sheet paper/ink, not white
- `2026-10-22` `3dcbb37` fix: no scrollbars in geology print side column
- `2026-10-22` `a233447` feat: analog photo for 百鹤玉; no hover credits on mineral photos
- `2026-10-22` `7aeaf1e` feat: mineral card lists each province's actual mineral kinds
- `2026-10-22` `067c3b8` chore: rename skill to tianditu-1m-atlas
- `2026-10-22` `eb54155` fix: init page on style.load, not only map 'load'
- `2026-10-25` `5221642` docs: add std cartographic generalization handbook
- `2026-10-25` `0b05952` docs: add label white-halo rule to carto handbook
- `2026-10-25` `deb7712` docs: add road/bridge label white-box rule to carto handbook
- `2026-10-25` `d27a434` docs: revert label white-box rule, keep thin halo only
- `2026-10-25` `80b78f3` feat: rename qianhu theme display name to 湖泊水网
- `2026-10-25` `9e0234f` docs: record z4 gate for major lakes, reservoirs and main rivers
- `2026-10-25` `ed33720` docs: add overlay rule and scenic-area label font to carto handbook
- `2026-10-25` `f83de1c` docs: record GB/T 20257.1 4.9 label fonts in carto handbook

### `atlas-earth`

- 提交数：`5`，区间：`2026-10-21` 至 `2026-10-23`
- `2026-10-21` `9e8765f` Initial commit
- `2026-10-21` `ebf8438` Add atlas-earth skill
- `2026-10-22` `131db87` Simplify atlas-earth skill wording.
- `2026-10-22` `5c87c5c` Add polygon clip support for atlas-earth skill.
- `2026-10-23` `467dde7` Add building replacement, atlas-style GLB notes, and clip vendor.

### `3d-building-map`

- 提交数：`5`，区间：`2026-06-17` 至 `2026-10-22`
- `2026-06-17` `076a97f` 避免路径错误
- `2026-06-17` `474cd4c` Merge branch 'main' of http://code.maptex.top/xcsmartdatabase/skills/3d-building-map
- `2026-06-18` `45de01a` 从maplibre-common获取脚本
- `2026-09-22` `12ed03b` feat: load map engines from GIS Agent /lib
- `2026-10-22` `1b35724` feat: sculpt WFC landmark and color/query by parent building

### `postgis-poi-address`

- 提交数：`2`，区间：`2026-10-10` 至 `2026-10-10`
- `2026-10-10` `1bf3208` init version
- `2026-10-10` `5238706` feat:add geojson result

### `mapgis-67`

- 提交数：`1`，区间：`2026-09-28` 至 `2026-09-28`
- `2026-09-28` `d1eb41e` feat:update skill

### `biodiversity-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `85acdd3` 从maplibre-common获取脚本
- `2026-09-22` `413822e` feat: load map engines from GIS Agent /lib
- `2026-09-22` `1a5bfb3` feat: switch Cesium product lib to 1.122
- `2026-09-24` `743c232` fix: keep Cesium logo and imagery credits visible

### `cobalt-mine-map`

- 提交数：`5`，区间：`2026-09-18` 至 `2026-09-24`
- `2026-09-18` `de6d164` Initial commit: cobalt-mine-map skill
- `2026-09-21` `206385d` docs: expand cobalt public data sources for investment assessment
- `2026-09-22` `92b0588` feat: load map engines from GIS Agent /lib
- `2026-09-22` `9293812` feat: switch Cesium product lib to 1.122
- `2026-09-24` `75bb769` fix: keep Cesium logo and imagery credits visible

### `coral-reef-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `64ca070` 从maplibre-common获取脚本
- `2026-09-22` `c8ab696` feat: load map engines from GIS Agent /lib
- `2026-09-22` `d50d650` feat: switch Cesium product lib to 1.122
- `2026-09-24` `c0cec92` fix: keep Cesium logo and imagery credits visible

### `earthquake-realtime-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `f43d598` 从maplibre-common获取脚本
- `2026-09-22` `ce9ffdc` feat: load map engines from GIS Agent /lib
- `2026-09-22` `ae8b53a` feat: switch Cesium product lib to 1.122
- `2026-09-24` `9988553` fix: keep Cesium logo and imagery credits visible

### `eonet-event-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `3891999` 从maplibre-common获取脚本
- `2026-09-22` `e9cfab9` feat: load map engines from GIS Agent /lib
- `2026-09-22` `182fe76` feat: switch Cesium product lib to 1.122
- `2026-09-24` `492e802` fix: keep Cesium logo and imagery credits visible

### `fishing-zone-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `a34ed10` 从maplibre-common获取脚本
- `2026-09-22` `4c2464e` feat: load map engines from GIS Agent /lib
- `2026-09-22` `0df7085` feat: switch Cesium product lib to 1.122
- `2026-09-24` `9f27102` fix: keep Cesium logo and imagery credits visible

### `flight-tracker-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `158e107` 从maplibre-common获取脚本
- `2026-09-22` `3fb7de7` feat: load map engines from GIS Agent /lib
- `2026-09-22` `16f8b8a` feat: switch Cesium product lib to 1.122
- `2026-09-24` `71bd4bb` fix: keep Cesium logo and imagery credits visible

### `ndvi-vegetation-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `74a4934` 从maplibre-common获取脚本
- `2026-09-22` `9cb857e` feat: load map engines from GIS Agent /lib
- `2026-09-22` `ece5499` feat: switch Cesium product lib to 1.122
- `2026-09-24` `ed153d6` fix: keep Cesium logo and imagery credits visible

### `nightlight-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `fd8e205` 从maplibre-common获取脚本
- `2026-09-22` `b86d508` feat: load map engines from GIS Agent /lib
- `2026-09-22` `f6b9df4` feat: switch Cesium product lib to 1.122
- `2026-09-24` `bd1142f` fix: keep Cesium logo and imagery credits visible

### `ocean-current-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `b7418f7` 从maplibre-common获取脚本
- `2026-09-22` `406fd4a` feat: load map engines from GIS Agent /lib
- `2026-09-22` `c46733a` feat: switch Cesium product lib to 1.122
- `2026-09-24` `dd4ddd4` fix: keep Cesium logo and imagery credits visible

### `openmeteo-contour-forecast-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `f2319e5` 从maplibre-common获取脚本
- `2026-09-22` `fefd5ba` feat: load map engines from GIS Agent /lib
- `2026-09-22` `b722bb2` feat: switch Cesium product lib to 1.122
- `2026-09-24` `41fa57a` fix: keep Cesium logo and imagery credits visible

### `protected-area-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `be74026` 从maplibre-common获取脚本
- `2026-09-22` `1dd8f82` feat: load map engines from GIS Agent /lib
- `2026-09-22` `6c0b596` feat: switch Cesium product lib to 1.122
- `2026-09-24` `a43ba46` fix: keep Cesium logo and imagery credits visible

### `shipping-ais-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `be17c9e` 从maplibre-common获取脚本
- `2026-09-22` `6257e2a` feat: load map engines from GIS Agent /lib
- `2026-09-22` `bf8011d` feat: switch Cesium product lib to 1.122
- `2026-09-24` `70c66a0` fix: keep Cesium logo and imagery credits visible

### `stac-browser-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `894200d` 从maplibre-common获取脚本
- `2026-09-22` `ef1bc36` feat: load map engines from GIS Agent /lib
- `2026-09-22` `18639ea` feat: switch Cesium product lib to 1.122
- `2026-09-24` `45ac968` fix: keep Cesium logo and imagery credits visible

### `tide-gauge-map`

- 提交数：`4`，区间：`2026-06-18` 至 `2026-09-24`
- `2026-06-18` `cdb80b3` 从maplibre-common获取脚本
- `2026-09-22` `2c6b7f4` feat: load map engines from GIS Agent /lib
- `2026-09-22` `544fcfa` feat: switch Cesium product lib to 1.122
- `2026-09-24` `bca992c` fix: keep Cesium logo and imagery credits visible

### `typhoon-track-map`

- 提交数：`3`，区间：`2026-09-22` 至 `2026-09-24`
- `2026-09-22` `6d22d3c` feat: load map engines from GIS Agent /lib
- `2026-09-22` `895a496` feat: switch Cesium product lib to 1.122
- `2026-09-24` `cf94fd7` fix: keep Cesium logo and imagery credits visible

### `cesium-common`

- 提交数：`11`，区间：`2026-06-24` 至 `2026-09-23`
- `2026-06-24` `2ce08a7` Add cesium common skill
- `2026-06-24` `e9735ae` Fix Cesium Tianditu subdomain guidance
- `2026-06-24` `e903288` Refine Tianditu guidance wording
- `2026-06-24` `db48cd0` Document IFC EPSG4547 heading alignment
- `2026-06-25` `ebc17f7` Document Cesium mouse move handler
- `2026-07-03` `ccbfde3` Refine Cesium 3D Tiles guidance
- `2026-09-22` `774135c` feat: load map engines from GIS Agent /lib
- `2026-09-22` `ab375f1` feat: switch Cesium product lib to 1.122
- `2026-09-23` `18c3cf5` docs: filter 3D Tiles layers with Cesium3DTileStyle in 1.122
- `2026-09-23` `049ef99` docs: require Cesium 1.122 APIs in generated pages
- `2026-09-23` `c8bafc6` feat:add logo css visible

### `maplibre-common`

- 提交数：`5`，区间：`2026-06-18` 至 `2026-09-23`
- `2026-06-18` `7c31a2c` Add maplibre common skill
- `2026-06-24` `16159b2` 更新
- `2026-07-09` `08270cf` feat:fix tiantitu submains bug
- `2026-09-22` `2547fae` feat: load map engines from GIS Agent /lib
- `2026-09-23` `1621538` docs: require glyphs before text-field and sprite before icon-image

### `3d-terrain-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `ab153d8` 从maplibre-common获取脚本
- `2026-09-22` `09ee493` feat: load map engines from GIS Agent /lib

### `change-detection-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `43b8a38` 从maplibre-common获取脚本
- `2026-09-22` `db6ec1b` feat: load map engines from GIS Agent /lib

### `china-airport-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `1423f40` 从maplibre-common获取脚本
- `2026-09-22` `9fe48ff` feat: load map engines from GIS Agent /lib

### `china-historical-map`

- 提交数：`2`，区间：`2026-08-07` 至 `2026-09-22`
- `2026-08-07` `4eceb0d` Initial china historical map skill
- `2026-09-22` `36fa7db` feat: load map engines from GIS Agent /lib

### `china-metro-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `5d44785` 从maplibre-common获取脚本
- `2026-09-22` `239ff8e` feat: load map engines from GIS Agent /lib

### `city-isochrone-map`

- 提交数：`3`，区间：`2026-06-15` 至 `2026-09-22`
- `2026-06-15` `7ef55d7` 换会Valhalla接口
- `2026-06-18` `bf6b719` 从maplibre-common获取脚本
- `2026-09-22` `d359f7f` feat: load map engines from GIS Agent /lib

### `classic-hiking-route-map`

- 提交数：`3`，区间：`2026-06-15` 至 `2026-09-22`
- `2026-06-15` `a7d4d94` Initial classic hiking route map skill
- `2026-06-18` `31f96b0` 从maplibre-common获取脚本
- `2026-09-22` `d71dc57` feat: load map engines from GIS Agent /lib

### `map-poster-maker`

- 提交数：`5`，区间：`2026-06-10` 至 `2026-09-22`
- `2026-06-10` `28b7c69` 优化脚本位置
- `2026-06-15` `ccdd42e` 优化300dpi输出
- `2026-06-18` `19d4be2` 从maplibre-common获取脚本
- `2026-06-24` `b561c2f` 更新
- `2026-09-22` `2e04906` feat: load map engines from GIS Agent /lib

### `nowcasting-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `0c3ce4a` 从maplibre-common获取脚本
- `2026-09-22` `2bf031b` feat: load map engines from GIS Agent /lib

### `personal-footprint-map`

- 提交数：`5`，区间：`2026-08-26` 至 `2026-09-22`
- `2026-08-26` `0fe255f` 新增中国个人足迹地图技能
- `2026-08-26` `dd7bd9c` 压缩行政区 GeoJSON 数据
- `2026-08-27` `6cf7143` 缓存 GeoJSON 避免重复请求
- `2026-08-27` `3179c69` 增加地图数据加载进度条
- `2026-09-22` `c6b8d97` feat: load map engines from GIS Agent /lib

### `poi-heatmap-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `6e28cec` 从maplibre-common获取脚本
- `2026-09-22` `e357a30` feat: load map engines from GIS Agent /lib

### `route-navigation`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `d6b632c` 从maplibre-common获取脚本
- `2026-09-22` `70db3ae` feat: load map engines from GIS Agent /lib

### `sea-level-rise-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `bcf7224` 从maplibre-common获取脚本
- `2026-09-22` `33cfa5d` feat: load map engines from GIS Agent /lib

### `self-driving-escape-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `0f6ab92` 从maplibre-common获取脚本
- `2026-09-22` `62f36cc` feat: load map engines from GIS Agent /lib

### `statistical-thematic-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `df3e46b` 从maplibre-common获取脚本
- `2026-09-22` `c50b962` feat: load map engines from GIS Agent /lib

### `storymap-template`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `b1b4068` 从maplibre-common获取脚本
- `2026-09-22` `8db9909` feat: load map engines from GIS Agent /lib

### `tianditu-geocoder`

- 提交数：`2`，区间：`2026-06-16` 至 `2026-09-22`
- `2026-06-16` `4c3af72` Add Tianditu geocoder skill
- `2026-09-22` `0678131` feat: load map engines from GIS Agent /lib

### `tourism-heatmap`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `b37a1f7` 从maplibre-common获取脚本
- `2026-09-22` `6383a02` feat: load map engines from GIS Agent /lib

### `tourist-attraction-map`

- 提交数：`2`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `e03d847` 从maplibre-common获取脚本
- `2026-09-22` `0936344` feat: load map engines from GIS Agent /lib

### `weather-visualization-map`

- 提交数：`3`，区间：`2026-06-18` 至 `2026-09-22`
- `2026-06-18` `8d85ce7` 从maplibre-common获取脚本
- `2026-09-22` `498b2e6` feat: load map engines from GIS Agent /lib
- `2026-09-22` `886ebd9` feat: switch Cesium product lib to 1.122

### `spatial-analysis`

- 提交数：`1`，区间：`2026-09-19` 至 `2026-09-19`
- `2026-09-19` `8b2f9bf` feat: add offline spatial analysis skill
