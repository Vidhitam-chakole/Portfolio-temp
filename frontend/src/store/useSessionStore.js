import { create } from 'zustand'

const useSessionStore = create((set) => ({
  visitor: '',
  setVisitor: (visitor) => set({ visitor }),
  clearVisitor: () => set({ visitor: '' }),
}))

export default useSessionStore
