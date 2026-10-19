---
name: overlay-layout-patterns
description: "Use when useOverlay 훅 기반 오버레이(모달/드로어) 구현 패턴 가이드. Overlay.Template 사용법, 올바른 Props 정의, 금지 패턴을 포함합니다. 모달, 드로어, 오버레이, ActionModal, 삭제 확인 구현 시: covers overlay, layout, patterns, actionmodal, useoverlay"
---

---
name: overlay-layout-patterns
description: useOverlay 훅 기반 오버레이(모달/드로어) 구현 패턴 가이드. Overlay.Template 사용법, 올바른 Props 정의, 금지 패턴을 포함합니다. 모달, 드로어, 오버레이, ActionModal, 삭제 확인 구현 시 사용합니다. Do NOT use for 전체 화면 구현(implement-screen) 또는 Figma 컴포넌트 매칭(figma-to-tds).
metadata:
  version: 1.1.0
  category: execution
---

# Overlay 패턴 가이드

## useOverlay 훅 패턴 (권장)

### 동작 원리

```
openOverlay() → Zustand 스토어에 추가 → Overlay.Container가 자동 렌더링
→ onConfirm/onCancel 호출 → 스토어에서 제거 (자동 닫힘)
```

**자동 주입되는 props**: `appeared`, `onConfirm`, `onCancel`

### 올바른 컴포넌트 정의

```tsx
import { Overlay, type OverlayProps } from "@thakicloud/shared";

export interface MyDrawerProps extends Omit<OverlayProps, "onConfirm"> {
  itemName: string;
  onConfirm?: (result: SomeResult) => void;
}

export const MyDrawer = ({
  itemName,
  onConfirm,
  onCancel,
  ...restProps
}: MyDrawerProps) => {
  const handleConfirm = () => {
    onConfirm?.({ success: true });
  };

  return (
    <Overlay.Template
      {...restProps}
      title="My Drawer"
      onConfirm={handleConfirm}
      onCancel={onCancel}
    >
      {/* 콘텐츠 */}
    </Overlay.Template>
  );
};
```

### 호출 방법

```tsx
const { openOverlay } = useOverlay();

const result = await openOverlay({
  component: MyDrawer,
  props: { itemName: "My Item" },
  options: { type: "drawer-horizontal", size: "md" },
});
```

---

## 금지 패턴 (CRITICAL)

```tsx
// ❌ isOpen 상태 직접 관리 - 스토어가 관리하므로 불필요
type BadProps = {
  isOpen: boolean;
  onClose: () => void; // ← onCancel로 대체
};

// ❌ appeared 수동 전달
<Overlay.Template appeared={isOpen} />

// ❌ window.confirm() 사용
if (window.confirm("삭제하시겠습니까?")) { ... }
```

---

## Props 타입 패턴

```tsx
// 결과값 없는 경우
interface InfoDrawerProps extends Omit<OverlayProps, "onConfirm"> {
  data: SomeData;
}

// 결과값 있는 경우
interface FormDrawerProps extends Omit<OverlayProps, "onConfirm"> {
  initialData?: FormData;
  onConfirm?: (result: FormData) => void;
}
```

---

## 확인용 ActionModal

```tsx
const { openOverlay } = useOverlay();

const confi
